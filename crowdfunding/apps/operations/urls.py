"""crowdfunding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from operations.views import operation_center, operation_apply, operation_apply_1, operation_member, \
    operation_apply_2, operation_apply_3, operation_apply_4, user_love

urlpatterns = [
    url(r'^operation_center/$',operation_center,name='operation_center'),
    url(r'^operation_member/$',operation_member,name='operation_member'),
    url(r'^operation_apply/$',operation_apply,name='operation_apply'),
    url(r'^operation_apply_1/$',operation_apply_1,name='operation_apply_1'),
    url(r'^operation_apply_2/$',operation_apply_2,name='operation_apply_2'),
    url(r'^operation_apply_3/$',operation_apply_3,name='operation_apply_3'),
    url(r'^operation_apply_4/$',operation_apply_4,name='operation_apply_4'),
    url(r'^user_love/$',user_love,name='user_love'),

]
