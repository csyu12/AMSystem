from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger
from apps.app_users.models import UserProfile, UserOperateLog
from apps.app_users.forms import LoginForm, UserPwdModifyForm, UserInfoForm
from apps.utils.mixin_utils import LoginRequiredMixin
from AMWebsit.settings import per_page
import csv

# 定义普通用户初始密码
PWD = '123456'


# 定义用户的相关视图
# 用户登录
class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username').strip()
            pass_word = request.POST.get('password').strip()
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'users/login.html', {'msg': '账号或密码错误'})
        else:
            return render(request, 'users/login.html', {'msg': '账号或密码错误', 'login_form': login_form})


# 用户退出
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        response = redirect(reverse('app_users:user_login'))
        response.delete_cookie('username')
        return response


# 用户修改密码
class UserPwdModifyView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/user_pwd_modify.html')

    def post(self, request):
        user_pwd_modify_form = UserPwdModifyForm(request.POST)
        if user_pwd_modify_form.is_valid():
            user = UserProfile.objects.get(username=request.user.username)
            pwd1 = request.POST.get('pwd1').strip()
            pwd2 = request.POST.get('pwd2').strip()
            if pwd1 == pwd2:
                user.password = make_password(pwd1)
                user.save()
                return HttpResponseRedirect((reverse('app_users:user_login')))
            else:
                return render(request, 'users/user_pwd_modify.html', {'msg': '两次密码不一致！'})
        else:
            return render(request, 'users/user_pwd_modify.html', {'msg': '密码不能为空！',
                                                                  'user_pwd_modify_form': user_pwd_modify_form})


# 管理员对用户的操作相关视图（普通管理员可见）
# 用户列表
class UserListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        # 排除超级管理员
        if search:
            search = request.GET.get('search').strip()
            users = UserProfile.objects.filter(Q(username__icontains=search) | Q(staff_no__icontains=search)
                                               | Q(department__icontains=search) | Q(bg_telephone__icontains=search)
                                               | Q(mobile__icontains=search) | Q(email__icontains=search),
                                               is_superuser=0).order_by('-is_staff', 'staff_no')
        else:
            users = UserProfile.objects.filter(is_superuser=0).order_by('-is_staff', 'staff_no')

        # 分页功能实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(users, per_page=per_page, request=request)
        p_users = p.page(page)
        start = (int(page)-1) * per_page  # 避免分页后每行数据序号从1开始
        return render(request, 'users/user_list.html', {'p_users': p_users, 'start': start, 'search': search})


# 添加用户
class UserAddView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/user_add.html')

    def post(self, request):
        userinfo_form = UserInfoForm(request.POST)
        if userinfo_form.is_valid():
            username = request.POST.get('username').strip()
            staff_no = request.POST.get('staff_no').strip()
            department = request.POST.get('department').strip()
            bg_telephone = request.POST.get('bg_telephone').strip()
            mobile = request.POST.get('mobile').strip()
            email = request.POST.get('email').strip()
            is_admin = request.POST.get('is_admin')
            user = UserProfile.objects.filter(username=username)
            if user:
                return render(request, 'users/user_add.html', {'msg': '用户 '+username+' 已存在！'})
            else:
                new_user = UserProfile(username=username, staff_no=staff_no, password=make_password(PWD), department=department,
                                       bg_telephone=bg_telephone, mobile=mobile, email=email, is_admin=is_admin)
                new_user.save()
                return HttpResponseRedirect((reverse('app_users:user_list')))
        else:
            return render(request, 'users/user_add.html', {'msg': '输入错误！', 'userinfo_form': userinfo_form})


# 用户详情页
class UserDetailView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        return render(request, 'users/user_detail.html', {'user': user})


# 修改用户信息
class UserModifyView(LoginRequiredMixin, View):
    def post(self, request):
        userinfo_form = UserInfoForm(request.POST)
        user_id = int(request.POST.get('user_id'))
        user = UserProfile.objects.get(id=user_id)
        if userinfo_form.is_valid():
            username = request.POST.get('username').strip()
            # 用户名唯一，判断用户名是否已存在
            other_user = UserProfile.objects.filter(~Q(id=user_id), username=username)
            if other_user:
                return render(request, 'users/user_detail.html', {'user': user, 'msg': username+'用户名已存在！'})
            else:
                # 获取用户提交的修改信息
                user.username = request.POST.get('username').strip()
                user.staff_no = request.POST.get('staff_no').strip()
                user.department = request.POST.get('department').strip()
                user.bg_telephone = request.POST.get('bg_telephone').strip()
                user.mobile = request.POST.get('mobile').strip()
                user.email = request.POST.get('email').strip()
                user.is_admin = request.POST.get('is_admin')
                user.is_staff = request.POST.get('is_staff')
                user.save()     # 将用户提交的修改信息存入数据库
                return HttpResponseRedirect((reverse('app_users:user_list')))
        else:
            return render(request, 'users/user_detail.html', {'user': user, 'msg': '输入错误！',
                                                              'userinfo_form': userinfo_form})


# 重置用户密码
class UserResetPwd(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        user.password = make_password(PWD)
        user.save()
        return HttpResponseRedirect((reverse('app_users:user_list')))


# 用户删除
class UserDeleteView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        user.delete()
        return HttpResponseRedirect((reverse('app_users:user_list')))


# csv导出函数
def create_excel(columns, content, file_name):
    file_name = file_name + '.csv'
    # 定义Response Headers，选择导出时跳出弹窗
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    response.charset = 'gbk'

    # 写入csv文件，注意：列名和值的位置要一一匹配
    csv_wr = csv.writer(response)
    csv_wr.writerow(columns)
    for i in content:
        i['is_admin'] = '是' if i['is_admin'] == '1' else '否'
        i['is_superuser'] = '是' if i['is_superuser'] == 1 else '否'
        i['is_staff'] = '是' if i['is_staff'] == '1' else '否'
        csv_wr.writerow([i['staff_no'], i['department'], i['bg_telephone'],
                         i['mobile'], i['is_admin'], i['is_superuser'],
                         i['is_staff'], i['modify_time']])
    return response


# 用户导出
class UserExportView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        # 排除超级管理员
        if search:
            search = request.GET.get('search').strip()
            users = UserProfile.objects.filter(Q(username__icontains=search) | Q(staff_no__icontains=search)
                                               | Q(department__icontains=search) | Q(bg_telephone__icontains=search)
                                               | Q(mobile__icontains=search) | Q(email__icontains=search,
                                               is_superuser=0)).order_by('-is_staff', 'staff_no')
        else:
            users = UserProfile.objects.filter(is_superuser=0).order_by('-is_staff', 'staff_no')
        users = users.values('staff_no', 'department', 'bg_telephone', 'mobile',
                             'is_admin', 'is_superuser', 'is_staff', 'modify_time')
        columns_names = ['工号', '部门', '办公电话', '手机号码', '管理员', '超级管理员', '在职', '修改时间']
        return create_excel(columns_names, users, 'Users')


# 操作日志视图(所有用户可见)
class UserOperateView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if search:
            search = search.strip().upper()
            operate_logs = UserOperateLog.objects.filter(Q(username__icontains=search) | Q(scope__icontains=search)
                                                         | Q(type__icontains=search)).order_by('-modify_time')
        else:
            operate_logs = UserOperateLog.objects.all().order_by('-modify_time')

        # 分页功能实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(operate_logs, per_page=per_page, request=request)
        p_operate_logs = p.page(page)
        start = (int(page)-1) * per_page  # 避免分页后每行数据序号从1开始

        return render(request, 'users/operate_log.html', {'operate_logs': p_operate_logs, 'start': start,
                                                          'search': search})



