from django.db import models
from datetime import datetime
# Create your models here.
from operations.models import UserAddress
from projects.models import Projects, SupportItems
from users.models import UserProfile

#该行代码，是得到系统配置的UserProfi类的实例对象
# UserProfile = get_user_model()


#我的支持等同于我的订单
class UserSupport(models.Model):
    # 订单号, 唯一：order_sn
    order_sn = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name='订单号')
    support_man = models.ForeignKey(UserProfile,verbose_name='支持人')
    support_project = models.ForeignKey(Projects,verbose_name='支持项目')
    support_item = models.ForeignKey(SupportItems,verbose_name='支持的回报项目')
    support_nums = models.IntegerField(default=0,verbose_name='支持数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='支持时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.support_man.username

    class Meta:
        verbose_name = '用户支持订单'
        verbose_name_plural = verbose_name


#订单信息
class OrderInfo(models.Model):
    PAY_STATUS = (
        ('PAYING','未支付'),
        ('TRADE_SUCCESS','支付成功'),
        ('FAIL','支付失败')
    )
    # 用户：user
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    #回报项目
    support_item = models.ForeignKey(SupportItems, verbose_name='支持的回报项目')

    item_nums = models.IntegerField(default=0,verbose_name='回报数量')

    # 订单号, 唯一：order_sn
    order_sn = models.CharField(max_length=30,unique=True,null=True,blank=True, verbose_name='订单号')
    # 交易号（与支付宝或者微信支付相关）：trade_no
    trade_no = models.CharField(max_length=30, unique=True, null=True, blank=True, verbose_name='交易号')
    # 订单总金额：order_mount
    order_mount = models.FloatField(default=0.0,verbose_name='订单总额')
    # 支付的状态（待支付，支付成功，支付失败）：pay_status
    pay_status = models.CharField(default='PAYING',max_length=30,choices=PAY_STATUS,verbose_name='支付状态')
    # 支付时间：pay_time
    pay_time = models.DateTimeField(null=True,blank=True,verbose_name='支付时间')
    # 订单留言：post_script
    post_script = models.CharField(max_length=200,null=True,blank=True,verbose_name='订单留言')
    #用户地址：address
    address = models.ForeignKey(UserAddress,verbose_name='用户地址')
    #是否需要发票
    need_invoice = models.BooleanField(default=False,verbose_name='是否需要发票')
    info_invoice = models.CharField(max_length=50,verbose_name='发票抬头')
    # 添加时间：add_time
    add_time =models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.order_sn

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
