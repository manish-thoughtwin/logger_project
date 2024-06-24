from django import forms
from .models import Registration

class SignupForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['first_name','last_name','email']
        
                
