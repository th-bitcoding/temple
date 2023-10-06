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
    primary_country = CountryField(blank_label="select country")
    primary_phone =models.CharField(max_length=11, null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    secondary_country = CountryField(blank_label="select country",blank=True,null=True,)
    secondary_phone = models.CharField(max_length=11, blank=True,null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    other_country = CountryField(blank_label="select country",blank=True,null=True,)
    other_phone = models.CharField(max_length=11,blank=True,null=True,validators=[RegexValidator(r'^\d{10,11}$','Number must be 10 or 11 digits','invalid number')],unique=True)
    email = models.EmailField(unique=True)
    secondary_email = models.EmailField(unique=True)
    DOB = models.DateField(default=None,null=True)
    first_name = models.CharField(max_length=100,null=True)
    middle_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=100,null=True)
    grand_father_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=6,choices=gender_choices, null=True)
    marriage_date = models.DateField(blank=True)
    blood_group = models.CharField(max_length=3, choices=blood_group_choice,null=True)

    def __str__(self):
        return self.first_name
    

class Business(models.Model):
    occupation_chices =(
        ('job','job'),
        ('bussiness','bussiness'),

    )
    address_type_choices=(
        ('home','home'),
        ('office','office')
    )
    username = models.ForeignKey(Registration,on_delete=models.CASCADE, default=None)
    occupation = models.CharField(max_length=255, null=True)
    occupation_type = models.CharField(max_length=9,choices=occupation_chices)
    education = models.CharField(max_length=255,blank=True, null=True)
    address_share_with = models.CharField(max_length=255,blank=True, null=True)
    share_phone_number = models.CharField(max_length=13,blank=True, null=True)
    address_type = models.CharField(max_length=6,choices=address_type_choices)
    address_1 = models.CharField(max_length=60, null=True)
    address_2 = models.CharField(max_length=60, blank=True, null=True)
    address_3 = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    taluka = models.CharField(max_length=50, null=True)
    city_or_village = models.CharField(max_length=50, null=True)
    zip_code =models.CharField(max_length=6, null=True,validators=[RegexValidator(r'^\d{6}$','Number must be 6 digits','invalid input')])

    def __str__(self):
        return self.username.username if self.username.username else ""
    

class Admission(models.Model):
    hostel_choices = (
        ('Kaveri','Kaveri'),
        ('Tapi','Tapi'),
        ('Saraswati','Saraswati')
    )
    username = models.ForeignKey(Registration,on_delete=models.CASCADE,default=None)

    standard =models.CharField(max_length=4, blank=True, null=True)
    ssc_gr_no =models.CharField(max_length=15, blank=True, null=True)
    hostel=models.CharField(max_length=10,choices=hostel_choices)
    hr_no = models.CharField(max_length=15, blank=True, null=True)
    hsc_year = models.DateField()
    ssc_year = models.DateField()

    def __str__(self):
        return self.username.username if self.username.username else ""
    

class Admissionreference(models.Model):
    hear_choices = (
        ('friend','friend'),
        ('news paper','news paper'),
        ('social sites','social sites'),
        ('others','others')
    )
    category_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C')
    )
    branch_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )
    member_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )
    sabha_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )

    username = models.ForeignKey(Registration,on_delete=models.CASCADE,default=None)
    Hear = models.CharField(max_length=20,choices=hear_choices)
    refernces = models.CharField(max_length=255,blank=True, null=True)
    category = models.CharField(max_length=50,choices=category_choices)
    skills = models.TextField(blank=True, null=True)
    branch = models.CharField(max_length=50,choices=branch_choices)
    member = models.CharField(max_length=50,choices=member_choices)
    sabha = models.CharField(max_length=50,choices=sabha_choices)

    def __str__(self):
        return self.username.username if self.username.username else "" 
    

class Relation(models.Model):
    relation_choices = (
        ('mother','mother'),
        ('father','father'),
        ('brother','brother'),
        ('daughter','daughter'),
        ('friend','friend')
    )
    username = models.ForeignKey(Registration,on_delete=models.CASCADE,default=None)
    relations = models.CharField(max_length=10,choices=relation_choices)
    relative_name = models.CharField(max_length=50, null=True)
    share_phone_number = models.CharField(max_length=10,null=True,validators=[RegexValidator(r'^\d{10}$','Phone Number must be 10 digits','invalid input')])

    def __str__(self):
        return self.relations
    

class Document(models.Model):
    document_choices = (
        ('Adhar','Adhar'),
        ('Pancard','Pancard'),
        ('Driving Licence','Driving Licence')
        
    )
    type_choices = (
        ('A','A'),
        ('B','B'),
        ('C','C')
        
    )
    is_private_choices = (
        ('Yes','Yes'),
        ('No','No'),
        
        
    )
    deceased_choices = (
        ('Yes','Yes'),
        ('No','No'),
        
    )
    username = models.ForeignKey(Registration,on_delete=models.CASCADE,default=None)
    Documents = models.CharField(max_length=50,choices=document_choices)
    document_no = models.CharField(max_length=15,blank=True, null=True)
    file = models.FileField(upload_to='doc/')
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50,choices=type_choices)
    is_private = models.CharField(max_length=3,choices=is_private_choices)
    deceased = models.CharField(max_length=3,choices=deceased_choices)

    def __str__(self):
        return self.username.username
    

















