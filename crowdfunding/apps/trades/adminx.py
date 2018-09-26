from django.contrib import admin
import xadmin
# Register your models here.
from trades.models import UserSupport, OrderInfo


class UserSupportAdmin(object):
    list_display = ['order_sn','support_man','support_project','support_item','support_nums',
                    'add_time','update_time','is_delete']


class OrderInfoAdmin(object):
    list_display = ['user','support_item','order_sn','trade_no','order_mount','pay_status','pay_time',
                    'post_script','address','need_invoice','info_invoice','add_time']



xadmin.site.register(UserSupport,UserSupportAdmin)
xadmin.site.register(OrderInfo,OrderInfoAdmin)


