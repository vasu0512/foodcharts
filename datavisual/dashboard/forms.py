from django import forms
from . models import fooddata

class foodForm(forms.ModelForm):
    class Meta:
        model=  fooddata
        fields='__all__'