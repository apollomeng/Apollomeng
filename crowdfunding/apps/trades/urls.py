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

from trades.views import trade_step1, trade_step2, trade_order,add_address,order_last

urlpatterns = [
    url(r'^trade_step1/(\d+)/$',trade_step1,name='trade_step1'),
    url(r'^trade_step2/(\d+)/$',trade_step2,name='trade_step2'),
    url(r'^trade_order/$',trade_order,name='trade_order'),
    url(r'^add_address/$',add_address,name='add_address'),
    url(r'^order_last/$',order_last,name='order_last'),


]
