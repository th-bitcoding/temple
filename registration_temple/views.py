from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .models import *
# Create your views here.
def index(request):
    return HttpResponse('hello django')


class RegistrationApi(APIView):
    permission_classes =[]
    def get_queryset(self):
        return Registration.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = RegistrationSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = RegistrationSerializers(data = request.data)
        if serializer.is_valid():
            email_check = request.data.get('primary_email')
            if email_check.endswith('.com') or email_check.endswith('.in') or ('@' in email_check):
                new_data = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid email format'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BussinessApi(APIView):
    permission_classes =[]
    def get_queryset(self):
        return Business.objects.all()
    
    def get(self,request,*args,**kwargs):
        queryset =self.get_queryset()
        serializer = BusinessSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializers = BusinessSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AdmissionApi(APIView):
    permission_classes =[]
    def get_queryset(self):
        return Admission.objects.all()
    
    def get(self,request,*args,**kwargs):
        queryset =self.get_queryset()
        serializer = AdmissionSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializers = AdmissionSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
class referenceApi(APIView):
    permission_classes =[]
    def get_queryset(self):
        return reference.objects.all()
    
    def get(self,request,*args,**kwargs):
        queryset =self.get_queryset()
        serializer = ReferenceSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializers = ReferenceSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RelationApi(APIView):
    permission_classes =[]
    def get_queryset(self):
        return Relation.objects.all()
    
    def get(self,request):
        queryset = self.get_queryset()
        serializers = RelationSerializers(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = RelationSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DocumentApi(APIView):
    permission_classes =[]
    def get_queryset(self):
        return Document.objects.all()
    
    def get(self,request):
        queryset = self.get_queryset()
        serializers = DocumentSerializers(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = DocumentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

            
