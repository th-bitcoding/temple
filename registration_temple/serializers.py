from rest_framework import serializers
from .models import *


class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class BusinessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class AdmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'

class ReferenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = reference
        fields = '__all__'

class RelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'
        
class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

