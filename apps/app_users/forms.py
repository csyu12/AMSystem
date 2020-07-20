from django import forms
from .models import UserProfile


# 通过Django内置forms组件校验用户的输入
# 定义登录时表单验证
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


# 定义用户修改密码时表单验证
class UserPwdModifyForm(forms.Form):
    pwd1 = forms.CharField(required=True)
    pwd2 = forms.CharField(required=True)


# 定义添加，修改用户时表单验证
class UserInfoForm(forms.ModelForm):
    username = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['staff_no', 'department', 'is_admin', 'bg_telephone', 'mobile']
