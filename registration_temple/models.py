from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import *
from django.core.validators import RegexValidator,MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
# Create your models here.

class Registration(AbstractUser,MyModel):

    gender_choices = (
        ("", "Gender"), 
        ('Male','Male'),
        ('Female','Female')
    )
    blood_group_choice=(
        ("", "Blood Group"), 
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-'),
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=True, 
        null=True   
    )
    primary_country = CountryField(blank_label="select country",default='IN')
    primary_phone =models.CharField(max_length=11, null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    secondary_country = CountryField(blank_label="select country",blank=True,null=True,)
    secondary_phone = models.CharField(max_length=11, blank=True,null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    other_country = CountryField(blank_label="select country",blank=True,null=True,)
    other_phone = models.CharField(max_length=11,blank=True,null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    secondary_email = models.EmailField(blank=True)
    DOB = models.DateField(default=None,null=True)
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=100,null=True)
    grand_father_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=6,choices=gender_choices, null=True)
    marriage_date = models.DateField(blank=True, null=True)
    blood_group = models.CharField(max_length=3, choices=blood_group_choice,null=True)

    def __str__(self):
        return self.email if self.email else ""
    

class Business(models.Model):
    occupation_chices =(
         ("", "Occupation"), 
        ('job','job'),
        ('bussiness','bussiness'),

    )
    address_type_choices=(
         ("", "Address"), 
        ('home','home'),
        ('office','office')
    )
    registration = models.ForeignKey(Registration,on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255, null=True)
    occupation_type = models.CharField(max_length=9,choices=occupation_chices)
    education = models.CharField(max_length=255,null=True)
    address_share_with = models.CharField(max_length=255,blank=True, null=True)
    share_phone_number = models.CharField(max_length=11,null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    address_type = models.CharField(max_length=6,choices=address_type_choices)
    address_1 = models.CharField(max_length=60, null=True)
    address_2 = models.CharField(max_length=60, blank=True, null=True)
    address_3 = models.CharField(max_length=60, blank=True, null=True)
    country = CountryField(default='IN')
    state = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    taluka = models.CharField(max_length=50, null=True)
    city_or_village = models.CharField(max_length=50, null=True)
    zip_code =models.CharField(max_length=6, null=True,validators=[RegexValidator(r'^\d{6}$','Number must be 6 digits','invalid input')])

    def __str__(self):
        return self.registration.first_name if self.registration.first_name else ""
    
class StudentStatus(models.Model):
    status_choice =(
         ("", "Select"), 
        ('Yes','Yes'),
        ('No','No')
    )
    student = models.ForeignKey(Registration, on_delete=models.CASCADE)
    student_status = models.CharField(choices=status_choice,default='Yes')

    def __str__(self):
        return self.student.email if self.student.email else ""

class EducationDetail(models.Model):
    hostel_choices = (
         ("", "Hostel"), 
        ('Kaveri','Kaveri'),
        ('Tapi','Tapi'),
        ('Saraswati','Saraswati')
    )

    student = models.ForeignKey(Registration,on_delete=models.CASCADE)
    standard =models.CharField(max_length=4, null=True)
    ssc_gr_no =models.CharField(max_length=15, null=True)
    hsc_gr_no =models.CharField(max_length=15, null=True)
    hostel=models.CharField(max_length=10,choices=hostel_choices)
    hr_no = models.CharField(max_length=15, blank=True, null=True)
    hsc_year = models.DateField(default=None,null=True)
    ssc_year = models.DateField(default=None,null=True)

    def __str__(self):
        return self.student.email if self.student.email else ""
    

class Admissionreference(models.Model):
    hear_choices = (
         ("", "Select"), 
        ('friend','friend'),
        ('news paper','news paper'),
        ('social sites','social sites'),
        ('others','others')
    )
    category_choices = (
         ("", "Select"), 
        ('A','A'),
        ('B','B'),
        ('C','C')
    )
    branch_choices = (
         ("", "Select"), 
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )
    member_choices = (
         ("", "Select"), 
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )
    sabha_choices = (
         ("", "Select"), 
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )

    student = models.ForeignKey(Registration,on_delete=models.CASCADE)
    Hear = models.CharField(max_length=20,choices=hear_choices)
    refernces = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=50,choices=category_choices)
    skills = models.CharField(max_length=100,null=True)
    branch = models.CharField(max_length=50,choices=branch_choices)
    member = models.CharField(max_length=50,choices=member_choices)
    sabha = models.CharField(max_length=50,choices=sabha_choices)

    def __str__(self):
        return self.student.email if self.student.email else "" 
    

class Student_Relative(models.Model):
    relation_choices = (
         ("", "Select"), 
        ('mother','mother'),
        ('father','father'),
        ('brother','brother'),
        ('daughter','daughter'),
        ('friend','friend')
    )
    student = models.ForeignKey(Registration,on_delete=models.CASCADE)
    relations = models.CharField(max_length=10,choices=relation_choices)
    relative_name = models.CharField(max_length=50, null=True)
    share_phone_number = models.CharField(max_length=10,null=True,validators=[RegexValidator(r'^\d{10}$','Phone Number must be 10 digits','invalid input')])

    def __str__(self):
        return self.student.email
    

class Document(models.Model):
    document_choices = (
        ("", "Select"), 
        ('Adhar','Adhar'),
        ('Pancard','Pancard'),
        ('Driving Licence','Driving Licence'),
        ('Others','Others')
        
    )
    type_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )
    is_private_choices = (
        ("", "Select"), 
        ('Yes','Yes'),
        ('No','No'),
        
        
    )
    deceased_choices = (
        ('Yes','Yes'),
        ('No','No'),
    )
    studentdocument = models.ForeignKey(Registration,on_delete=models.CASCADE)
    Documents = models.CharField(max_length=50,choices=document_choices)
    document_no = models.CharField(max_length=15,null=True)
    file = models.FileField(upload_to='doc/',null=True)
    comment = models.CharField(max_length=100,blank=True, null=True)
    type = models.CharField(max_length=50,choices=type_choices,default='A')
    is_private = models.CharField(max_length=3,choices=is_private_choices)
    deceased = models.CharField(max_length=3,choices=deceased_choices)

    def __str__(self):
        return self.studentdocument.email
    

















