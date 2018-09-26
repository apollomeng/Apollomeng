from django.http import JsonResponse
from django.shortcuts import render, redirect,reverse
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
# Create your views here.
# from operations.models import UserProject
from projects.forms import ProjectsForm, SupportItemsForm, Supportstep3Form
from projects.models import Projects, ProjectsCategory, ProjectsDetailImage, SupportItems


def project_list(request):
    all_projects = Projects.objects.all()
    category_all = ProjectsCategory.objects.all()

    search = request.GET.get('search','')
    if search:
        all_projects = all_projects.filter(name__contains=search)

    #根据类别过滤
    cate = request.GET.get('cate','')
    if cate:
        all_projects = all_projects.filter(category_id=int(cate))
    # 根据状态过滤
    stat = request.GET.get('stat','')
    if stat:
        all_projects = all_projects.filter(status=stat)
    # 根据综合过滤
    sort = request.GET.get('sort','')
    if sort == 'time':
        all_projects = all_projects.order_by('-add_time')
    if sort == 'funding':
        all_projects = all_projects.order_by('-target_funding')
    if sort == 'support':
        all_projects = all_projects.order_by('-support_num')



    pa = Paginator(all_projects,4)
    pagenum = request.GET.get('pagenum','')
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return render(request,'projects/project_list.html',{
        'all_projects': all_projects,
        'category_all': category_all,
        'pages': pages,
        'cate': cate,
        'stat': stat,
        'sort': sort,
        'search': search,
    })


def project_detail(request,proid):
    if proid:
        project = Projects.objects.filter(id=proid)[0]
        return render(request,'projects/project_detail.html',{
            'project':project
        })

def project_start(request):
    return  render(request,'projects/project_start.html')


#众筹第一步
def project_start_step1(request):
    if request.method == 'POST':
        project_step1_form = ProjectsForm(request.POST,request.FILES)
        if project_step1_form.is_valid():
            name = project_step1_form.cleaned_data['name']
            title_image = project_step1_form.cleaned_data['title_image']
            detail_image = request.FILES.get('detail_image')
            category = project_step1_form.cleaned_data['category']
            desc = project_step1_form.cleaned_data['desc']
            target_funding = project_step1_form.cleaned_data['target_funding']
            due_days = project_step1_form.cleaned_data['due_days']
            user_detail = project_step1_form.cleaned_data['user_detail']
            user_mobile = project_step1_form.cleaned_data['user_mobile']
            user_desc = project_step1_form.cleaned_data['user_desc']
            service_mobile = project_step1_form.cleaned_data['service_mobile']

            project = Projects()
            project.name = name
            project.title_image = title_image
            project.desc = desc
            project.target_funding = target_funding
            project.due_days = due_days
            project.user_detail = user_detail
            project.user_mobile = user_mobile
            project.user_desc = user_desc
            project.service_mobile = service_mobile
            cate = ProjectsCategory.objects.filter(name=category)[0]
            project.category = cate

            project.save()

            project_detail_image = ProjectsDetailImage()
            project_detail_image.detail_image = detail_image
            project_detail_image.project = project
            project_detail_image.save()

            proid = project.id

            # return render(request,'projects/project_start_step2.html',{
            #     'project':project,
            # })
            #重定向到第二步
            return redirect(reverse('projects:project_start_step2',args=[proid]))
        else:
            return render(request, 'projects/project_start_step1.html', {
                'project_step1_form': project_step1_form
            })
    else:
        category_lists = ProjectsCategory.objects.all()
        return render(request, 'projects/project_start_step1.html', {
            'category_lists': category_lists
        })


#众筹第二步
def project_start_step2(request,proid):
    if proid:
        project = Projects.objects.filter(id=int(proid))[0]
        if request.method == 'GET':
            support_item_lists = SupportItems.objects.filter(project_id=int(proid))
            # support_item_lists = [item.supportitem for item in project_support_lists]
            return render(request, 'projects/project_start_step2.html',{
                'support_item_list':support_item_lists,
                'project':project
            })
        else:
            support_items_form = SupportItemsForm(request.POST,request.FILES)
            if support_items_form.is_valid():
                suppor_funding = support_items_form.cleaned_data['suppor_funding']
                category = support_items_form.cleaned_data['category']
                desc = support_items_form.cleaned_data['desc']
                image = support_items_form.cleaned_data['image']
                nums = support_items_form.cleaned_data['nums']
                is_restrict = support_items_form.cleaned_data['is_restrict']
                restrict_nums = support_items_form.cleaned_data['restrict_nums']
                transport_cost = support_items_form.cleaned_data['transport_cost']
                is_invoice = support_items_form.cleaned_data['is_invoice']
                result_time = support_items_form.cleaned_data['result_time']

                support_item = SupportItems()

                support_item.category = category
                support_item.support_funding = suppor_funding
                support_item.desc = desc
                support_item.image = image
                support_item.nums = nums
                support_item.is_restrict = is_restrict
                support_item.restrict_nums = restrict_nums
                support_item.transport_cost = transport_cost
                support_item.is_invoice = is_invoice
                support_item.result_time = result_time

                support_item.project = project
                support_item.save()

                # project_support = ProjectsSupportItem()
                # project_support.project = project
                # project_support.supportitem = support_item
                # project_support.save()

                proid = project.id

                return redirect(reverse('projects:project_start_step2',args=[proid]))
            else:
                print('验证出错了')
                return redirect(reverse('projects:project_start_step1'))
    else:
        print('没有项目id')
        return redirect(reverse('projects:project_start_step1'))

#众筹第三步
def project_start_step3(request,proid):
    #众筹第三步
    if proid:
        project = Projects.objects.filter(id=int(proid))[0]
        if request.method == 'GET':
            return render(request, 'projects/project_start_step3.html',{
                'project':project
            })
        else:
            support_step3_form = Supportstep3Form(request.POST)
            if support_step3_form.is_valid():
                yigou_zhanghao = support_step3_form.cleaned_data['yigou_zhanghao']
                faren_id =support_step3_form.cleaned_data['faren_id']
                project.yigou_zhanghao = yigou_zhanghao
                project.faren_id = faren_id
                project.project_man = request.user
                project.project_status = True
                project.save()

                return redirect(reverse('projects:project_start_step4'))



def project_start_step4(request):
    return render(request, 'projects/project_start_step4.html')

