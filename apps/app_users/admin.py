from django.contrib import admin
from .models import UserProfile, UserOperateLog


# 后台用户信息表相关设置
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # 设置列表显示的属性
    list_display = ['username', 'staff_no', 'department', 'bg_telephone', 'mobile',
                    'is_admin', 'is_superuser', 'is_staff', 'modify_time']
    # 设置允许搜索关键字
    search_fields = ['username', 'staff_no', 'mobile']
    # 排序，负号表示降序
    ordering = ['-staff_no']
    # 设置可直接编辑的字段
    list_editable = ['is_admin']
    # 列表分页，设置支持最大显示行
    list_per_page = 5
    # 设置支持进入编辑界面的字段，默认第一个字段
    list_display_links = []

    # 设置编辑页显示的属性以及排序
    fields = ['username', 'staff_no', 'department', 'bg_telephone', 'mobile',
              'is_admin', 'is_superuser', 'is_staff', 'modify_time']

    # 过滤器
    list_filter = ['department', 'is_admin']
    # 按时间分层
    date_hierarchy = 'modify_time'

    actions_on_bottom = True  # 底部显示删除动作选项
    actions_on_top = False  # 删除头部动作选项


# 后台用户操作日志表相关设置
# 日志暂不需要给后台权限，防止篡改
# @admin.register(UserOperateLog)
# class UserOperateLogAdmin(admin.ModelAdmin):
#     pass


