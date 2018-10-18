from django import forms

from .models import Vendor, Food
from django.utils.translation import gettext_lazy as _

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
            # fields = (
            #         'vendor_name',
            #         'store_name',
            #         'phone_number',
            #         'address',
            # )
        labels = {
            'vendor_name': _('攤販名稱'),
            'store_name' : _('店名'),
            'phone_number' : _('電話'),
            'address' : _('地址'),
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
