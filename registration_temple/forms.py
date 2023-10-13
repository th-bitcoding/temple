from django import forms
from django.forms import widgets
from .models import *
from django.forms.widgets import SelectDateWidget
from django.utils import timezone
# from bootstrap_datepicker_plus import DatePickerInput
import datetime

class RegistrationForm(forms.ModelForm):
    DOB = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datepicker',
            "placeholder" :"Date Of Birth"
        })
    )
    marriage_date = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            "placeholder" :"Marriage Date",
            # 'required': 'false',
        }), required=False
    )
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
        self.fields['blood_group'].empty_label = None

class RegistrationBusiness(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['occupation_type','occupation','education','address_share_with','share_phone_number','address_type','address_1','address_2','address_3','country','state','district','taluka','city_or_village','zip_code']
        widgets = {
            'occupation_type': forms.Select(attrs={'class':'gender-control'}),
            'occupation':forms.TextInput(attrs={"placeholder": "Occupation"}),
            'address_type': forms.Select(attrs={'class':'gender-control'}),
            'country':forms.Select(attrs={"class": "gender-control"}),
            'education':forms.TextInput(attrs={"placeholder": "Education"}),
            'address_share_with':forms.TextInput(attrs={"placeholder": "Address Share With"}),
            'share_phone_number':forms.TextInput(attrs={"placeholder": "Share Phone Number"}),
            'address_1':forms.TextInput(attrs={"placeholder": "Address 1"}),
            'address_2':forms.TextInput(attrs={"placeholder": "Address 2"}),
            'address_3':forms.TextInput(attrs={"placeholder": "Address 3"}),
            'address_3':forms.TextInput(attrs={"placeholder": "Address 3"}),
            'state':forms.TextInput(attrs={"placeholder": "State"}),
            'district':forms.TextInput(attrs={"placeholder": "District"}),
            'taluka':forms.TextInput(attrs={"placeholder": "Taluka"}),
            'city_or_village':forms.TextInput(attrs={"placeholder": "City/Village"}),
            'zip_code':forms.TextInput(attrs={"placeholder": "ZipCode"}),

        }

class StudentStatusForm(forms.ModelForm):
    class Meta:
        model = StudentStatus
        fields = ['student_status']
        widgets = {
            'student_status':forms.Select(attrs={"class":"gender-control"})
        }

class StudentEducationForm(forms.ModelForm):
    hsc_year = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datepicker1',
            "placeholder" :"HSC Year"
        })
    )
    ssc_year = forms.DateField(
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datepicker',
            "placeholder" :"SSC Year",
            # 'required': 'false',
        })
    )
    class Meta:
        model = EducationDetail
        fields = ['standard','ssc_gr_no','hsc_gr_no','hostel','hr_no','hsc_year','ssc_year']
        widgets = {
            'hostel':forms.Select(attrs={"class":"gender-control"}),
            'ssc_gr_no':forms.TextInput(attrs={'placeholder':'SSC Gr No'}),
            'hsc_gr_no':forms.TextInput(attrs={'placeholder':'HSC Gr No'}),
            'hr_no':forms.TextInput(attrs={'placeholder':'Hr No'}),
            'standard':forms.TextInput(attrs={'placeholder':'Standard'}),
        }

class StudentNewForm(forms.ModelForm):
    class Meta:
        model = Admissionreference
        fields=['id','Hear','refernces','category','skills','branch','member','sabha']
        widgets = {
            'Hear':forms.Select(attrs={"class":"gender-control"}),
            'category':forms.Select(attrs={"class":"gender-control"}),
            'branch':forms.Select(attrs={"class":"gender-control"}),
            'member':forms.Select(attrs={"class":"gender-control"}),
            'sabha':forms.Select(attrs={"class":"gender-control"}),
            'refernces':forms.TextInput(attrs={'placeholder':'Reference'}),
            'skills':forms.TextInput(attrs={'placeholder':'Skills'}),
            'ssc_gr_no':forms.TextInput(attrs={'placeholder':'SSC Gr No'}),


        }


class StudentRelationForm(forms.ModelForm):
    class Meta:
        model = Student_Relative
        fields=['id','relations','relative_name','share_phone_number']
        widgets = {
            'relations':forms.Select(attrs={"class":"gender-control"}),
            'relative_name':forms.TextInput(attrs={'placeholder':'Relative Name'}),
            'share_phone_number':forms.TextInput(attrs={'placeholder':'Phone Number'}),
        }

class StudentDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['id','Documents','document_no','file','comment','type','is_private','deceased']
        widgets = {
            'Documents':forms.Select(attrs={"class":"gender-control"}),
            'file':forms.FileInput(attrs={"class":"file-control"}),
            'type':forms.Select(attrs={"class":"gender-control"}),
            'is_private':forms.Select(attrs={"class":"gender-control"}),
            'deceased':forms.Select(attrs={"class":"gender-control"}),
            'comment':forms.TextInput(attrs={"placeholder":"Comment"})

        }