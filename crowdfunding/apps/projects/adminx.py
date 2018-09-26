from django.contrib import admin
import xadmin
# Register your models here.
from projects.models import ProjectsCategory, Projects, ProjectsDetailImage, IndexCategoryAd, SupportItems, BannerInfo


class ProjectsCategoryAdmin(object):
    list_display = ['name','desc','add_time']


class ProjectsAdmin(object):
    list_display = ['name','category','target_funding','status','due_days','desc','add_time','dead_time',
                    'click_num','love_num','support_num','user_desc','service_mobile','project_man','project_status']


class ProjectsDetailImageAdmin(object):
    list_display = ['project','add_time']


class IndexCategoryAdAdmin(object):
    list_display = ['project','index','add_time']


class SupportItemsAdmin(object):
    list_display = ['category','project','support_funding','nums','supported_nums','is_restrict','transport_cost','is_invoice','is_delete','add_time']

class BannerInfoAdmin(object):
    list_display = ['image','url','add_time']


xadmin.site.register(BannerInfo,BannerInfoAdmin)
xadmin.site.register(ProjectsCategory,ProjectsCategoryAdmin)
xadmin.site.register(Projects,ProjectsAdmin)
xadmin.site.register(ProjectsDetailImage,ProjectsDetailImageAdmin)
xadmin.site.register(IndexCategoryAd,IndexCategoryAdAdmin)
xadmin.site.register(SupportItems,SupportItemsAdmin)

