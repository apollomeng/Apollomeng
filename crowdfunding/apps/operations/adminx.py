from django.contrib import admin
import xadmin
# Register your models here.
from operations.models import UserLove,UserAddress


class UserLoveAdmin(object):
    list_display = ['love_man','love_project','love_status','add_time']


# class UserProjectAdAdmin(object):
#     list_display = ['project_man','project','project_status','add_time']


class UserAddressAdmin(object):
    list_display = ['user','address','signer_name','signer_mobile','address_nums','add_time']



xadmin.site.register(UserLove,UserLoveAdmin)
# xadmin.site.register(UserProject,UserProjectAdAdmin)
xadmin.site.register(UserAddress,UserAddressAdmin)

