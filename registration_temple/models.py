from django.db import models

# Create your models here.
class Registration(models.Model):

    gender_choices = (
        ('Male','Male'),
        ('Female','Female')
    )

    primary_country = models.CharField(max_length=255, blank=True, null=True)
    primary_phone = models.CharField(max_length=255, blank=True, null=True)
    secondary_country = models.CharField(max_length=255, blank=True, null=True)
    secondary_phone = models.CharField(max_length=255, blank=True, null=True)
    other_country = models.CharField(max_length=255, blank=True, null=True)
    other_phone = models.CharField(max_length=255, blank=True, null=True)
    primary_email = models.EmailField(unique=True)
    secondary_email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    grand_father_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=6,choices=gender_choices)
    marriage_date = models.DateField()
    blood_group = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.primary_country
    
class Business(models.Model):
    occupation_chices =(
        ('job','job'),
        ('bussiness','bussiness'),

    )
    address_type_choices=(
        ('home','home'),
        ('office','office')
    )
    occupation = models.CharField(max_length=255, blank=True, null=True)
    occupation_type = models.CharField(max_length=9,choices=occupation_chices)
    education = models.CharField(max_length=255,blank=True, null=True)
    address_share_with = models.CharField(max_length=255,blank=True, null=True)
    share_phone_number = models.CharField(max_length=13,blank=True, null=True)
    address_type = models.CharField(max_length=6,choices=address_type_choices)
    address_1 = models.CharField(max_length=60, blank=True, null=True)
    address_2 = models.CharField(max_length=60, blank=True, null=True)
    address_3 = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    taluka = models.CharField(max_length=50, blank=True, null=True)
    city_or_village = models.CharField(max_length=50, blank=True, null=True)
    zip_code =models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.occupation
    

class Admission(models.Model):
    school_choices =(
        ('gurukul','gurukul'),
        ('BMU','BMU'),
        ('vanita vishram','vanita vishram'),
        ('others','others')
    )
    hostel_choices = (
        ('Kaveri','Kaveri'),
        ('Tapi','Tapi'),
        ('Saraswati','Saraswati')
    )

    school = models.CharField(max_length=15,choices=school_choices)
    standard =models.CharField(max_length=4, blank=True, null=True)
    ssc_gr_no =models.CharField(max_length=15, blank=True, null=True)
    hostel=models.CharField(max_length=10,choices=hostel_choices)
    hr_no = models.CharField(max_length=15, blank=True, null=True)
    hsc_year = models.DateField()
    ssc_year = models.DateField()

    def __str__(self):
        return self.school
    
class reference(models.Model):
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
    refernces = models.CharField(max_length=255,blank=True, null=True)
    category = models.CharField(max_length=50,choices=category_choices)
    skills = models.TextField(blank=True, null=True)
    branch = models.CharField(max_length=50,choices=branch_choices)
    member = models.CharField(max_length=50,choices=member_choices)
    sabha = models.CharField(max_length=50,choices=sabha_choices)

    def __str__(self):
        return self.refernces
    
class Relation(models.Model):
    relation_choices = (
        ('mother','mother'),
        ('father','father'),
        ('daughter','daughter')
    )
    relations = models.CharField(max_length=10,choices=relation_choices)
    relative = models.CharField(max_length=50,blank=True, null=True)
    share_phone_number = models.CharField(max_length=13,blank=True,null=True)

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
    Documents = models.CharField(max_length=50,choices=document_choices)
    document_no = models.CharField(max_length=15,blank=True, null=True)
    file = models.FileField(upload_to='doc/')
    comment = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50,choices=type_choices)
    is_private = models.CharField(max_length=3,choices=is_private_choices)
    deceased = models.CharField(max_length=3,choices=deceased_choices)

    def __str__(self):
        return self.Documents















