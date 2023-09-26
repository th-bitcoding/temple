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
    class Meta:
        model = Admission
        fields = '__all__'


class AdmissionreferenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admissionreference
        fields = '__all__'


class RelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'


class DocumentSerializers(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    class Meta:
        model = Document
        fields = ['id','username','Documents','document_no','file','comment','type','is_private','deceased']

    def get_username(self,obj):
        return obj.username.username

