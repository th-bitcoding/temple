from django import forms
from django.forms import widgets
from .models import *
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
# from bootstrap_datepicker_plus import DatePickerInput
import datetime

class RegistrationForm(forms.ModelForm):
    # DOB = forms.DateField(widget=forms.SelectDateWidget())
    def clean_DOB(self):
        dob = self.cleaned_data.get('DOB')
        if dob and dob > timezone.now().date():
            raise forms.ValidationError("Date of Birth cannot be in the future.")
        return dob
    

    class Meta:
        model = Registration
        fields =['primary_country','primary_phone','secondary_country','secondary_phone','other_country','other_phone','email','secondary_email','DOB','first_name','middle_name','last_name','grand_father_name','gender','marriage_date','blood_group']
        widgets = {
            "gender": forms.Select(attrs={"class": "gender-control"}),
            "blood_group": forms.Select(attrs={"class": "gender-control"}),
            "primary_country": forms.Select(attrs={"class": "gender-control"}),
            "secondary_country": forms.Select(attrs={"class": "gender-control"}),
            "other_country": forms.Select(attrs={"class": "gender-control"}),
             "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
             "middle_name": forms.TextInput(attrs={"placeholder": "Middle Name"}),
             "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
             "primary_phone": forms.TextInput(attrs={"placeholder": "Primary Phone"}),
             "secondary_phone": forms.TextInput(attrs={"placeholder": "Secondary Phone"}),
             "other_phone": forms.TextInput(attrs={"placeholder": "Other Phone"}),

             "email": forms.TextInput(attrs={"placeholder": "Email"}),
             "secondary_email": forms.TextInput(attrs={"placeholder": "Secondary Email"}),
             "grand_father_name": forms.TextInput(attrs={"placeholder": "Grand Father Name"}),

        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['DOB'].widget = forms.DateInput(attrs={'class': 'input-dob', 'type': 'date',  'placeholder':"Date Of Birth"})
        self.fields['marriage_date'].widget = forms.DateInput(attrs={'class': 'input-dob', 'type': 'date', 'placeholder':"Marriage Date"})
        self.fields['blood_group'].empty_label = None


     
    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     data = Registration.objects.filter(email=email).exists()
    #     if not data:
    #         raise forms.ValidationError("Email ALready Exist")
    #     return data


        # cleaned_data = self.clean()
        # first_name = cleaned_data.get('first_name')
        # if int in first_name:  # You create this function
        #     self.add_error('first_name', "Insert Valid")
        # return first_name