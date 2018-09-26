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
from projects.views import project_detail, project_list, project_start, project_start_step1, project_start_step2, \
    project_start_step3,project_start_step4



urlpatterns = [
    url(r'^project_detail/(\d+)/$',project_detail,name='project_detail'),
    url(r'^project_list/$',project_list,name='project_list'),
    url(r'^project_start/$',project_start,name='project_start'),
    url(r'^project_start_step1/$',project_start_step1,name='project_start_step1'),
    url(r'^project_start_step2/(\d+)/$',project_start_step2,name='project_start_step2'),
    url(r'^project_start_step3/(\d+)/$',project_start_step3,name='project_start_step3'),
    url(r'^project_start_step4/$',project_start_step4,name='project_start_step4'),

]
