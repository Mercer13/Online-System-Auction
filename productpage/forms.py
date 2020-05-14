from django import forms
from .models import Product

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('itemname','description','image','initialbid' )