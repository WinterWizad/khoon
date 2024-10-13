from django import forms 
from .models import Doners

class DonerForm(forms.ModelForm):
    class Meta:
        model=Doners
        fields='name','age','phone','blood','address','photo'

        #fields='__all__'      
        