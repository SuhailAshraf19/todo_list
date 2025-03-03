from django import forms
from .models import List, Items

class ListForm(forms.ModelForm):
    class Meta:
        model= List
        fields=['name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields=['name']        