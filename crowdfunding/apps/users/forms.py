from django import forms
from .models import UserProfile


class UserProfileForm(forms.Form):
    name = forms.CharField(required=True,min_length=4,error_messages={
        'required':'用户名必须填写',
        'min_length':'用户名不少于4位',
    })
    password = forms.CharField(required=True,max_length=20, min_length=3, error_messages={
        'required': '密码必须填写',
        'max_length':'密码不超过20位',
        'min_length':'密码不少于3位',
    })
    email = forms.CharField(required=True, min_length=8, error_messages={
        'required': '邮箱必须填写',
        'min_length': '邮箱不少于8位',
    })

class UserLoginForm(forms.Form):
    name = forms.CharField(required=True, min_length=4, error_messages={
        'required': '用户名必须填写',
        'min_length': '用户名不少于4位',
    })
    password = forms.CharField(required=True, max_length=20, min_length=3, error_messages={
        'required': '密码必须填写',
        'max_length': '密码不超过20位',
        'min_length': '密码不少于3位',
    })
