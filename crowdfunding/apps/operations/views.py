from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect,reverse

# Create your views here.
from helptools.send_email_tools import send_email_code
from operations.forms import OperationApply1Form, OperationApply2Form, OperationApply3Form, OperationApply4Form
# from operations.models import UserProject
from operations.models import UserLove
from projects.models import Projects
from trades.models import UserSupport, OrderInfo
from users.models import VerifyCode, UserProfile


#我的众筹
def operation_center(request):
    user = request.user
    user_projects = Projects.objects.filter(project_man_id=user.id,is_delete=False)
    user_orders = UserSupport.objects.filter(support_man=request.user,is_delete=False)
    user_loves = UserLove.objects.filter(love_man=request.user,love_status=True)
    return render(request, 'operations/operation_center.html',{
        'user_projects':user_projects,
        'user_orders':user_orders,
        'user_loves':user_loves,
        # 'user':user,
    })

#我的资产
def operation_member(request):
    return render(request, 'operations/operation_member.html')



#认证过程
def operation_apply(request):
    return render(request,'operations/operation_apply.html')

def operation_apply_1(request):
    if request.method == 'GET':
        return render(request,'operations/operation_apply_1.html')
    else:
        operation_apply1_form = OperationApply1Form(request.POST)
        if operation_apply1_form.is_valid():
            real_name = operation_apply1_form.cleaned_data['real_name']
            phone = operation_apply1_form.cleaned_data['phone']
            id_card_num = operation_apply1_form.cleaned_data['id_card_num']

            user = request.user
            user.real_name = real_name
            user.phone = phone
            user.id_card_num = id_card_num
            user.save()

            return render(request,'operations/operation_apply_2.html')
        else:
            print('验证出错')
            return render(request,'operations/operation_apply_1.html')


def operation_apply_2(request):
    if request.method == 'GET':
        return render(request,'operations/operation_apply_2.html')
    else:
        operation_apply2_form = OperationApply2Form(request.POST,request.FILES)
        if operation_apply2_form.is_valid():
            image = operation_apply2_form.cleaned_data['image']

            user = request.user
            user.image = image
            user.save()

            return render(request, 'operations/operation_apply_3.html')
        else:
            print('验证出错')
            return render(request, 'operations/operation_apply_2.html')

def operation_apply_3(request):
    if request.method == 'GET':
        return render(request,'operations/operation_apply_3.html')
    else:
        operation_apply3_form = OperationApply3Form(request.POST)
        if operation_apply3_form.is_valid():
            email = operation_apply3_form.cleaned_data['email']

            user = request.user
            user.email = email
            user.save()

            #发送验证码
            send_email_code(email)

            return render(request, 'operations/operation_apply_4.html')
        else:
            print('验证出错')
            return render(request, 'operations/operation_apply_3.html')

def operation_apply_4(request):
    if request.method == 'GET':
        return render(request, 'operations/operation_apply_4.html')
    else:
        operation_apply4_form = OperationApply4Form(request.POST)
        if operation_apply4_form.is_valid():
            code = operation_apply4_form.cleaned_data['code']
            email_ver = VerifyCode.objects.filter(code=code)[0]
            email = email_ver.email
            user = UserProfile.objects.filter(email=email)
            if user:
                user[0].is_verify = True
                user[0].save()
                email_ver.delete()
                return redirect(reverse('operations:operation_center'))
            else:
                return HttpResponse('发送验证码的用户不存在')



        return render(request, 'operations/operation_apply_4.html')


def user_love(request):
    love_id = request.GET.get('love_id', '')

    ty = Projects.objects.filter(id=int(love_id))[0]

    if love_id :
        love = UserLove.objects.filter(love_man=request.user, love_project_id=int(love_id))
        if love:
            if love[0].love_status:
                love[0].love_status = False
                love[0].save()
                ty.love_num -= 1
                ty.save()

                return JsonResponse({'status': 'ok', 'msg': '关注'})
            else:
                love[0].love_status = True
                love[0].save()
                ty.love_num += 1
                ty.save()
                return JsonResponse({'status': 'ok', 'msg': '取消关注'})
        else:
            a = UserLove()
            a.love_man = request.user
            a.love_project_id = love_id
            a.love_status = True
            a.save()
            ty.love_num += 1
            ty.save()
            return JsonResponse({'status': 'ok', 'msg': '取消关注'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '收藏失败'})

