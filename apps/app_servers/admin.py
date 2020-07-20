from django.contrib import admin
from .models import Server, ServerType, ServerHis


# 后台资产表相关设置
@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    # 设置列表显示的属性
    list_display = ['zctype', 'ipaddress', 'description', 'brand', 'zcmodel',
                    'zcnumber', 'zcpz', 'owner', 'undernet', 'guartime',
                    'modify_time', 'comment']
    # 设置允许搜索关键字
    search_fields = ['zcnumber', 'ipaddress']
    # 排序，负号表示降序
    ordering = []
    # 设置可直接编辑的字段
    list_editable = ['comment']
    # 列表分页，设置最大显示行
    list_per_page = 8
    # 设置支持进入编辑界面的字段，默认第一个字段
    list_display_links = []

    # 设置编辑页显示的属性以及排序
    # fields = ['username', 'staff_no', 'department', 'bg_telephone', 'mobile',
    #           'is_admin', 'is_superuser', 'is_staff', 'modify_time']

    # 过滤器
    list_filter = ['zctype', 'brand', 'owner', 'undernet']
    # 按时间分层
    date_hierarchy = 'modify_time'

    actions_on_bottom = True  # 底部显示删除动作选项
    actions_on_top = False  # 删除头部动作选项


# 后台资产类型表相关设置
@admin.register(ServerType)
class ServerTypeAdmin(admin.ModelAdmin):
    # 设置允许搜索关键字
    search_fields = ['zctype']


# 后台资产历史表相关设置
# 历史记录暂时不给权限，防止篡改
# @admin.register(ServerHis)
# class ServerHisAdmin(admin.ModelAdmin):
#     pass
