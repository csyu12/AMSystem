from django.contrib import admin
from .models import Server, ServerType, ServerHis


# 后台资产表相关设置
@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    pass


# 后台资产类型表相关设置
@admin.register(ServerType)
class ServerTypeAdmin(admin.ModelAdmin):
    pass


# 后台资产历史表相关设置
# 历史记录暂时不给权限，防止篡改
# @admin.register(ServerHis)
# class ServerHisAdmin(admin.ModelAdmin):
#     pass
