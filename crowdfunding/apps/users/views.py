from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from projects.models import IndexCategoryAd, ProjectsCategory, Projects, BannerInfo
from users.forms import UserProfileForm,UserLoginForm
from users.models import UserProfile


def index(request):
    banners = BannerInfo.objects.all().order_by('index')[:3]
    ad_projects = IndexCategoryAd.objects.all().order_by('index')[:3]

    keji_id = ProjectsCategory.objects.filter(name='科技')[0].id
    sheji_id = ProjectsCategory.objects.filter(name='设计')[0].id
    gongyi_id = ProjectsCategory.objects.filter(name='公益')[0].id
    nongye_id = ProjectsCategory.objects.filter(name='农业')[0].id
    keji_projects = Projects.objects.filter(category_id=keji_id)[:4]
    sheji_projects = Projects.objects.filter(category_id=sheji_id)[:4]
    gongyi_projects = Projects.objects.filter(category_id=gongyi_id)[:4]
    nongye_projects = Projects.objects.filter(category_id=nongye_id)[:4]

    return render(request,'index.html',{
        'ad_projects':ad_projects,
        'banners':banners,
        'keji_projects':keji_projects,
        'sheji_projects':sheji_projects,
        'gongyi_projects':gongyi_projects,
        'nongye_projects':nongye_projects,
    })


def user_register(request):
    if request.method == 'GET':
        return render(request, 'users/user_register.html')
    else:
        user_register_form = UserProfileForm(request.POST)
        if user_register_form.is_valid():
            name = user_register_form.cleaned_data['name']
            password = user_register_form.cleaned_data['password']
            email = user_register_form.cleaned_data['email']

            user = UserProfile.objects.filter(username=name)
            if user:
                return render(request,'users/user_register.html',{
                    'msg':'用户名已存在'
                })
            else:
                user = UserProfile()
                user.username = name
                user.name = name
                user.set_password(password)
                user.email = email
                user.save()

                return render(request,'users/user_login.html')
        else:
            return render(request,'users/user_register.html',{
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request,'users/user_login.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            name = user_login_form.cleaned_data['name']
            password = user_login_form.cleaned_data['password']

            user = authenticate(username=name,password=password)
            if user:
                login(request,user)
                return redirect('index')
            else:
                return render(request,'users/user_login.html',{
                    'msg':'用户名或者密码错误'
                })
        else:
            return render(request, 'users/user_login.html', {
                'user_login_form': 'user_login_form'
            })

def user_logout(request):
    logout(request)
    return redirect(reverse('index'))

    ggggg
    yyyyy
    


