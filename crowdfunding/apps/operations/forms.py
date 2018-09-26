from django import forms
from .models import Projects


class OperationApply1Form(forms.Form):
    real_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    id_card_num = forms.CharField(required=True)



class OperationApply2Form(forms.Form):
    image = forms.ImageField(required=True)

class OperationApply3Form(forms.Form):
    email = forms.EmailField(required=True)

class OperationApply4Form(forms.Form):
    code = forms.CharField(required=True)

class UserAddressForm(forms.Form):
    address = forms.CharField(required=True)
    signer_name = forms.CharField(required=True)
    signer_mobile = forms.CharField(required=True)





