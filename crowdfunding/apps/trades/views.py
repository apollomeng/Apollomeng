from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse,HttpResponse
from datetime import datetime
# Create your views here.
from crowdfunding.settings import APPID, RETURN_URL, APP_PRIVATE_KEY_PATH, ALIPAY_PUBLIC_KEY_PATH, ALIPAY_DEBUG
from operations.forms import UserAddressForm
from operations.models import UserAddress
from projects.models import SupportItems
from trades.models import UserSupport, OrderInfo
from helptools.get_order_sn import get_order_sn
from utils.alipay import AliPay


def trade_step1(request,supid):
    if supid:
        supportitem = SupportItems.objects.filter(id=int(supid))[0]

        return render(request,'trades/trade_step1.html',{
            'supportitem':supportitem,
        })




def trade_order(request):
    num = request.GET.get('num','')
    supid = request.GET.get('supid','')

    if num and supid:

        supportitem = SupportItems.objects.filter(id=int(supid))[0]

        usersupport = UserSupport()
        usersupport.support_project = supportitem.project
        usersupport.support_man = request.user
        usersupport.support_item = supportitem
        usersupport.support_nums = num
        usersupport.order_sn = get_order_sn(request.user.id)
        usersupport.save()

        return JsonResponse({'status': 'ok', 'msg': '成功提交'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '失败'})


def trade_step2(request,supid):
    supportitem = SupportItems.objects.filter(id=int(supid))[0]
    usersupport = UserSupport.objects.filter(support_item_id=int(supid),support_man=request.user)[0]
    useraddress_list = UserAddress.objects.filter(user=request.user)

    order_mount = int(usersupport.support_nums) * int(supportitem.support_funding) + supportitem.transport_cost

    return render(request, 'trades/trade_step2.html', {
        'supportitem': supportitem,
        'usersupport': usersupport,
        'useraddress_list': useraddress_list,
        'order_mount': order_mount,
    })

def add_address(request):
    user_address_form = UserAddressForm(request.POST)

    if user_address_form.is_valid():
        address = user_address_form.cleaned_data['address']
        signer_name = user_address_form.cleaned_data['signer_name']
        signer_mobile = user_address_form.cleaned_data['signer_mobile']

        useraddress = UserAddress()
        useraddress.user = request.user
        useraddress.address  = address
        useraddress.signer_name  = signer_name
        useraddress.signer_mobile  = signer_mobile
        useraddress.save()


        return JsonResponse({'status': 'ok', 'msg': '成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '失败'})


def order_last(request):
    add_id = request.POST.get('add_id','')
    need_invoice = request.POST.get('need_invoice','')
    info_invoice = request.POST.get('info_invoice','个人')
    post_script = request.POST.get('post_script','无')
    supid = request.POST.get('supid','')
    order_mount = request.POST.get('order_mount','')

    useraddress = UserAddress.objects.filter(id=int(add_id))[0]
    supportitem = SupportItems.objects.filter(id=int(supid))[0]
    usersupport = UserSupport.objects.filter(support_item_id=int(supid))[0]

    orderinfo = OrderInfo()

    orderinfo.user = request.user
    orderinfo.support_item = supportitem
    orderinfo.item_nums = usersupport.support_nums
    orderinfo.order_sn = usersupport.order_sn
    orderinfo.order_mount = order_mount
    orderinfo.post_script = post_script
    orderinfo.address = useraddress
    if need_invoice =='option1':
        orderinfo.need_invoice =False
    else:
        orderinfo.need_invoice = True
        orderinfo.info_invoice = info_invoice

    orderinfo.save()

    # 得到支付的类
    alipay = AliPay(
        appid=APPID,
        # 支付宝服务器主动通知商户服务器里指定的页面http/https路径
        app_notify_url=RETURN_URL,
        app_private_key_path=APP_PRIVATE_KEY_PATH,
        alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=ALIPAY_DEBUG,  # 默认False,
        # 同步通知，回调这个地址
        return_url=RETURN_URL
    )
    url = alipay.direct_pay(
        subject=orderinfo.order_sn,
        out_trade_no=orderinfo.order_sn,
        total_amount=orderinfo.order_mount
    )
    # 沙箱环境
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    print('生成的支付连接：')
    print(re_url)

    return JsonResponse({'status': 'ok', 'msg': re_url})





#支付宝回调的验证：1，验证是否被修改，2，修改为已支付
def alipay(request):
    alipay = AliPay(
        appid=APPID,
        # 支付宝服务器主动通知商户服务器里指定的页面http/https路径
        app_notify_url=RETURN_URL,
        app_private_key_path=APP_PRIVATE_KEY_PATH,
        alipay_public_key_path=ALIPAY_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=ALIPAY_DEBUG,  # 默认False,
        # 同步通知，回调这个地址
        return_url=RETURN_URL
    )

    processed_query = {}

    for key, value in request.GET.items():
        processed_query[key] = value

    ali_sign = processed_query.pop('sign', None)

    check_result = alipay.verify(processed_query, ali_sign)

    print('get的验证情况', check_result)

    # 2 验证通过，修改成已支付
    if check_result:
        # 得到订单号
        order_sn = processed_query.get('out_trade_no', None)
        # 得到交易号
        trade_no = processed_query.get('trade_no', None)

        # 根据订单号查找订单
        order_info = OrderInfo.objects.filter(order_sn=order_sn)[0]

        # 设置交易号
        order_info.trade_no = trade_no
        # 设置交易状态
        order_info.pay_status = 'TRADE_SUCCESS'
        # 设置交易付款时间
        order_info.pay_time = datetime.now()

        order_info.save()

        # return Response('success')
        response = redirect('index')
        response.set_cookie('nextPath', 'pay', max_age=2)
        return response
    else:
        response = redirect('index')
        return response
