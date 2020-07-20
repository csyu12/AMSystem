from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# 在 http://brack3t.com/our-custom-mixins.html 网站看到了一个类，很好用
# 功能：让需要验证用户是否登录的类视图（views）继承，能自动验证用户是否已登录。若没登录，跳到login_required指定url
# 例如：在本项目中，用户想要进行资产管理，必须先登录，从而进行一系列业务处理
class LoginRequiredMixin(object):
    # method_decorator的作用是为函数视图装饰器补充第一个self参数，以适配类视图方法。
    @method_decorator(login_required(login_url='/users/login'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
