from rest_framework import serializers
from .models import *


class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = ['password', 'username']
       

class RegistrationUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = ['password', 'username','email']
        

class BusinessSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Business
        fields = ['id','occupation','occupation_type','education','address_share_with','share_phone_number','address_type','address_1','address_2','address_3','country','state','district','taluka','city_or_village','zip_code','username']
        # fields ='__all__'
        
    def get_username(self,obj):
        return obj.username.username


class AdmissionSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Admission
        fields = ['id','username','standard','ssc_gr_no','hostel','hr_no','hsc_year','ssc_year']

    def get_username(self,obj):
        return obj.username.username


class AdmissionreferenceSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Admissionreference
        fields = ['id','username','Hear','refernces','category','skills','branch','member','sabha']

    def get_username(self,obj):
        return obj.username.username


class RelationSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Relation
        fields = ['id','username','relations','relative_name','share_phone_number']

    def get_username(self,obj):
        return obj.username.username


class DocumentSerializers(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    class Meta:
        model = Document
        fields = ['id','username','Documents','document_no','file','comment','type','is_private','deceased']

    def get_username(self,obj):
        return obj.username.username
    
class EmailWorkSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmailCheckModel
        fields = '__all__'


