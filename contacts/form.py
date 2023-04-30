from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['first_name', 
                 'last_name', 
                 'email', 
                 'address_1', 
                 'address_2', 
                 'city', 
                 'state', 
                 'zipcode', 
                 'profile_pic']
        
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'})
        }
