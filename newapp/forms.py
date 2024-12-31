from django import forms 
from .models import Emergencies

class EmergenciesForm(forms.ModelForm):
    class Meta:
        model=Emergencies
        fields='name','age','hospital','blood','reason','photo'

        #fields='__all__'      
        