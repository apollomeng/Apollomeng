from django.core.mail import send_mail

from crowdfunding.settings import EMAIL_FROM
from users.models import VerifyCode
from random import randint


def get_email_code(code_length):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code +=code_source[randint(0,len(code_source)-1)]
    return code


def send_email_code(email):
    email_ver = VerifyCode()
    email_ver.email = email
    code = get_email_code(4)
    email_ver.code = code
    email_ver.save()

    # send_title = ''
    # send_body = ''

    send_title = '欢迎注册众筹网站'
    # send_body = '请点击以下链接进行验证:\n http://127.0.0.1:8000/users/user_active/'+code
    send_body = '请输入以下验证码:'+code
    send_mail(send_title,send_body,EMAIL_FROM,[email])
    #
    # if email_type == 'forget':
    #     send_title = '谷粒教育邮箱密码重置'
    #     send_body = '请点击以下链接进行激活:\n http://127.0.0.1:8000/users/user_resetpwd/'+code
    #     send_mail(send_title,send_body,EMAIL_FROM,[email])
    #
    # if email_type == 'change':
    #     send_title = '谷粒教育邮箱重置'
    #     send_body = '您的验证码：'+code
    #     send_mail(send_title,send_body,EMAIL_FROM,[email])




