from django import forms
from .models import Product,Box,invoice
class newform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pid']
class newform1(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['sku','quantity','box_type']
class newform2(forms.ModelForm):
    class Meta:
        model=invoice
        fields=['entry_date','invoice_number']

