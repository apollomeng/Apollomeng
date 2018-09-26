from django.contrib import admin
import xadmin
# Register your models here.
from users.models import VerifyCode
from xadmin import views

class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSiteSetting(object):
    site_title = '众筹网后台管理系统'
    site_footer = '众筹网'
    # menu_style = 'accordion'


class VerifyCodeAdmin(object):
    list_display = ['code','email','add_time']


xadmin.site.register(VerifyCode,VerifyCodeAdmin)

xadmin.site.register(views.BaseAdminView, BaseXadminSetting)
xadmin.site.register(views.CommAdminView, GlobalSiteSetting)