from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
# Create your models here.
from users.models import UserProfile
#该行代码，是得到系统配置的UserProfi类的实例对象
# UserProfile = get_user_model()

#项目类别表
class ProjectsCategory(models.Model):
    name = models.CharField(max_length=30,verbose_name='项目类别名称')
    desc = models.TextField(max_length=100, null=True, blank=True, verbose_name='商品详情', help_text='类别描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目类别'
        verbose_name_plural = verbose_name


#项目详情
class Projects(models.Model):
    PROJECTSTAUS =(
        ('即将开始','即将开始'),
        ('众筹中','众筹中'),
        ('众筹成功','众筹成功'),
    )
    project_man = models.ForeignKey(UserProfile,null=True,blank=True,verbose_name='项目发起人')
    project_status = models.BooleanField(default=False,verbose_name='项目是否确定发布')
    name = models.CharField(max_length=50,verbose_name='项目名称')

    category = models.ForeignKey(ProjectsCategory,verbose_name='项目类别')
    title_image = models.ImageField(upload_to='projects/%y/%m/%d',max_length=200,verbose_name='项目头图')
    target_funding = models.DecimalField(default=0,max_digits=10,decimal_places=2,verbose_name='筹资金额')
    support_funding = models.DecimalField(default=0,max_digits=10,decimal_places=2,verbose_name='支持金额')
    status = models.CharField(choices=PROJECTSTAUS,max_length=20,default='即将开始',verbose_name='项目状态')
    due_days = models.IntegerField(default=0,verbose_name='筹资天数')
    desc = models.TextField(max_length=100, null=True, blank=True,verbose_name='项目简介')
    detail = models.TextField(max_length=500, null=True, blank=True,verbose_name='项目详情说明')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    start_time = models.DateTimeField(default=datetime.now,verbose_name='开始时间')
    dead_time = models.DateTimeField(default=datetime.now, verbose_name='截止时间')
    is_delete = models.BooleanField(default=0,verbose_name='是否删除')

    click_num = models.IntegerField(default=0,verbose_name='点击量')
    love_num = models.IntegerField(default=0,verbose_name='关注人数')
    support_num = models.IntegerField(default=0,verbose_name='支持人数')
    user_desc = models.CharField(max_length=50,verbose_name='自我介绍')
    user_detail = models.TextField(max_length=500, null=True, blank=True,verbose_name='详情自我介绍')
    user_mobile = models.CharField(max_length=11,verbose_name='发起人电话')
    service_mobile = models.CharField(max_length=14,verbose_name='客服电话')

    yigou_zhanghao = models.CharField(max_length=18,null=True,blank=True,verbose_name='易付宝企业账号')
    faren_id = models.CharField(max_length=18,null=True,blank=True,verbose_name='法人身份证号')
    is_renzheng = models.BooleanField(default=0,verbose_name='是否认证')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目详情'
        verbose_name_plural = verbose_name

#项目详情照片
class ProjectsDetailImage(models.Model):
    project = models.ForeignKey(Projects,verbose_name='项目')
    detail_image = models.ImageField(upload_to='projects/detaili/%y/%m/%d',max_length=200,verbose_name='项目详情图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = '项目详情图片'
        verbose_name_plural = verbose_name

#首页广告位
class IndexCategoryAd(models.Model):
    project = models.ForeignKey(Projects,verbose_name='所属项目')
    index = models.IntegerField(default=1, verbose_name='广告项目顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = '首页广告项目'
        verbose_name_plural = verbose_name


#项目可以支持的回报方式
class SupportItems(models.Model):
    SUPPORTSCATEGORY = (
        ('实物回报','实物回报'),
        ('虚拟物品回报','虚拟物品回报')
    )
    project = models.ForeignKey(Projects,verbose_name='所属项目')
    category = models.CharField(choices=SUPPORTSCATEGORY,max_length=20,verbose_name='回报类型')
    support_funding = models.DecimalField(max_digits=8,decimal_places=2,verbose_name='支持金额')
    desc = models.TextField(max_length=200,verbose_name='回报内容')
    image= models.ImageField(upload_to='supports/%y/%m/%d',verbose_name='回报说明图片')
    nums = models.IntegerField(default=0,verbose_name='回报数量')
    supported_nums = models.IntegerField(default=0,verbose_name='此回报已获支持数量')

    is_restrict = models.BooleanField(default=0,verbose_name='是否限购')
    restrict_nums = models.IntegerField(default=1,verbose_name='限购数量')
    transport_cost = models.IntegerField(default=0,verbose_name='运费')
    is_invoice = models.BooleanField(default=0,verbose_name='是否开发票')
    result_time= models.IntegerField(default=0,verbose_name='回报时间')
    is_delete = models.BooleanField(default=0,verbose_name='是否删除')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = '回报项目'
        verbose_name_plural = verbose_name


class BannerInfo(models.Model):
    image = models.ImageField(upload_to='banners/%y/%m/%d',max_length=200,verbose_name='首页轮播图片')
    project = models.ForeignKey(Projects,verbose_name='所属项目')
    index = models.IntegerField(default=1, verbose_name='图片顺序')
    url = models.URLField(max_length=200,verbose_name='轮播链接')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name='轮播信息'
        verbose_name_plural = verbose_name