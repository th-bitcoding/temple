from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display =['id','first_name','primary_country']

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display =['id','occupation']

@admin.register(StudentStatus)
class StudentStatusAdmin(admin.ModelAdmin):
    list_display =['id','student_status']

@admin.register(EducationDetail)
class AdmissionAdmin(admin.ModelAdmin):
    list_display =['id','hostel']

@admin.register(Admissionreference)
class referenceAdmin(admin.ModelAdmin):
    list_display =['id','refernces']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display =['id','Documents']

@admin.register(Student_Relative)
class RelationAdmin(admin.ModelAdmin):
    list_display =['id','relations']



