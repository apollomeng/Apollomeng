from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class UserProfile(AbstractUser):
    VERIFY_TYPE = (
        (1,'商业公司'),
        (2,'个体工商户'),
        (3,'个人经营'),
        (4,'政府及非营利组织'),
    )

    image = models.ImageField(upload_to='users/%y/%m/%d',max_length=200,verbose_name='用户头像')
    name = models.CharField(max_length=50, verbose_name='姓名', help_text='姓名')
    birthday = models.DateTimeField(null=True,blank=True,verbose_name='用户生日')
    gender = models.CharField(choices=(('男','男'),('女','女')),max_length=10,default='男',verbose_name='性别')
    phone = models.CharField(max_length=11,verbose_name='手机号')
    is_verify = models.BooleanField(default=False,verbose_name='是否认证')
    verify_type = models.CharField(choices=VERIFY_TYPE,max_length=10,verbose_name='认证类型')
    real_name = models.CharField(max_length=20,verbose_name='身份证姓名')
    id_card_num = models.CharField(max_length=18,null=True,blank=True,verbose_name='身份证号')
    id_card_image = models.ImageField(max_length=18,null=True,blank=True,verbose_name='身份证照片')
    email = models.EmailField(max_length=18,null=True,blank=True,verbose_name='邮箱')

    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class VerifyCode(models.Model):
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    code = models.CharField(max_length=20,verbose_name='验证码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '验证码信息'
        verbose_name_plural = verbose_name






