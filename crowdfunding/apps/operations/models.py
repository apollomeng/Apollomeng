from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
# Create your models here.
from projects.models import Projects
from users.models import UserProfile
#该行代码，是得到系统配置的UserProfi类的实例对象
# UserProfile = get_user_model()

#用户关注的项目
class UserLove(models.Model):
    love_man = models.ForeignKey(UserProfile,verbose_name='关注人')
    love_project = models.ForeignKey(Projects,verbose_name='关注项目')
    love_status = models.BooleanField(default=False,verbose_name='关注状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='关注时间')

    def __str__(self):
        return self.love_man.username

    class Meta:
        verbose_name = '关注信息'
        verbose_name_plural = verbose_name


#用户地址
class UserAddress(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户')
    # 用户：user
    # 地址：address
    address = models.CharField(max_length=50,verbose_name='地址')
    # 签收人：singer_name
    signer_name = models.CharField(max_length=30, verbose_name='签收人')
    # 签收电话：singer_mobile
    signer_mobile = models.CharField(max_length=11, verbose_name='签收人电话')
    address_nums = models.IntegerField(default=1,verbose_name='地址数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户收货地址'
        verbose_name_plural = verbose_name
