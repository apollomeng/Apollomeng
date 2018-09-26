from django import forms
from .models import Projects


class ProjectsForm(forms.Form):
    name = forms.CharField(required=True)
    category = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    target_funding = forms.IntegerField(required=True)
    due_days = forms.IntegerField(required=True)
    title_image = forms.ImageField(required=True)
    user_detail = forms.CharField(required=True)
    user_mobile = forms.CharField(required=True)
    user_desc = forms.CharField(required=True)
    service_mobile = forms.CharField(required=True)


class SupportItemsForm(forms.Form):
    suppor_funding = forms.DecimalField(required=True)
    category = forms.CharField(required=True)
    desc = forms.CharField(required=True)
    image = forms.ImageField(required=True)
    nums = forms.IntegerField(required=True)
    is_restrict = forms.BooleanField(required=True)
    restrict_nums = forms.IntegerField(required=True)
    transport_cost = forms.IntegerField(required=True)
    is_invoice = forms.BooleanField(required=True)
    result_time = forms.IntegerField(required=True)


class Supportstep3Form(forms.Form):
    yigou_zhanghao = forms.CharField(required=True)
    faren_id = forms.CharField(required=True)

