from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display =['id','first_name','email','primary_country']

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display =['username','id','occupation']

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display =['id','username']

@admin.register(Admissionreference)
class referenceAdmin(admin.ModelAdmin):
    list_display =['id','refernces']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display =['id','Documents']

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display =['id','relations']



