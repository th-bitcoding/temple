import random
import string
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .models import *
from rest_framework.exceptions import APIException
# Create your views here.
def index(request):
    return HttpResponse('hello django')


class RegistrationApi(APIView):
    permission_classes =[]
    def getuser(self,pk):
        try:
            return Registration.objects.get(pk=pk)
        except Registration.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get_queryset(self):
        return Registration.objects.all()

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = RegistrationSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = RegistrationSerializers(data = request.data)
        if serializer.is_valid():
            email=serializer.validated_data['email']
            username = email.split('@')[0]
            password = username + ''.join([random.choice(string.digits) for i in range(0, 3)])
            user = serializer.save(username = username ,password=password)
            print('username',username)
            print('password',password)
            user.set_password(password)
            user.save()
           
            return Response({'detail': 'User created successfully', 'username': username}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        snippet = self.getuser(pk)
        serializer = RegistrationUpdateSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        snippet = self.getuser(pk)
        snippet.delete()
        return Response({'message':'Delete Successfully'},status=status.HTTP_204_NO_CONTENT)
    

class BussinessApi(APIView):
    permission_classes =[]
    def getuser(self,pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get_queryset(self):
        return Business.objects.all()
    
    def get(self,request,*args,**kwargs):
        queryset =self.get_queryset()
        serializer = BusinessSerializers(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializers = BusinessSerializers(data=request.data)
        if serializers.is_valid():
            username = request.data.get('username')
            print('username',username)
            try:
                new_id=Registration.objects.get(username = username)
            except Registration.DoesNotExist:
                return Response({'error':'Does Not Exist'},status=status.HTTP_404_NOT_FOUND)
            
            serializers.save(username=new_id)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        snippet = self.getuser(pk)
        serializers = BusinessSerializers(snippet,data=request.data)
        if serializers.is_valid():
            username = request.data.get('username')
            print('username',username)
            try:
                new_id= Registration.objects.get(username = username)
            except Registration.DoesNotExist:
                return Response({'error':'Username Does Not Exist'},status=status.HTTP_404_NOT_FOUND)

            serializers.save(username = new_id)
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        snippet = self.getuser(pk)
        snippet.delete()
        return Response({'message':'Delete Successfully'},status=status.HTTP_204_NO_CONTENT)
    

class AdmissionApi(APIView):
    permission_classes =[]
    def getuser(self,pk):
        try:
            return Admission.objects.get(pk=pk)
        
        except Admission.DoesNotExist:
            return None
    
    def get(self,request,*args,**kwargs):
        flag=request.query_params.get('flag')
        print('flag',flag)
        if flag == "Yes" or flag=="yes":
            queryset =Admission.objects.all()
            serializer = AdmissionSerializers(queryset,many=True)
            return Response(serializer.data)
        else:
            queryset =Admissionreference.objects.all()
            serializer = AdmissionreferenceSerializers(queryset,many=True)
            return Response(serializer.data)
        
    def post(self,request):
        flag=request.query_params.get('flag')
        print('flag',flag)
        if flag == "Yes" or flag == "yes":
            serializers = AdmissionSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            serializers = AdmissionreferenceSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        snippet = self.getuser(pk)
        serializers = AdmissionSerializers(snippet,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,*args,**kwargs):
        new = self.kwargs['pk']
        snippet = self.getuser(new)
        snippet.delete()
        return Response({'message':'Delete Successfully'},status=status.HTTP_204_NO_CONTENT)

    
# class referenceApi(APIView):
#     permission_classes =[]
#     def get_queryset(self):
#         return reference.objects.all()
    
#     def get(self,request,*args,**kwargs):
#         queryset =self.get_queryset()
#         serializer = ReferenceSerializers(queryset,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializers = ReferenceSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RelationApi(APIView):
    permission_classes =[]

    def getuser(self,pk):
        try:
            return Relation.objects.get(pk=pk)
        except Relation.DoesNotExist:
            return None
    
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
    
    def put(self,request,pk):
        snippet = self.getuser(pk)
        serializers = RelationSerializers(snippet,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,*args,**kwargs):
        new = self.kwargs['pk']
        snippet = self.getuser(new)
        snippet.delete()
        return Response({'message':'Delete Successfully'},status=status.HTTP_204_NO_CONTENT)
    

class DocumentApi(APIView):
    permission_classes =[]
    def getuser(self,pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            return None
    
    def get_queryset(self):
        return Document.objects.all()
    
    def get(self,request):
        queryset = self.get_queryset()
        serializers = DocumentSerializers(queryset,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = DocumentSerializers(data=request.data)
        if serializers.is_valid():
            username = request.data.get('username')
            # print('username',username)
            check = Registration.objects.get(username=username)
            serializers.save(username = check)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        snippet = self.getuser(pk)
        serializers = DocumentSerializers(snippet,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        snippet = self.getuser(pk)
        snippet.delete()
        return Response({'message':'Delete Successfully'},status=status.HTTP_204_NO_CONTENT)


    
    
    

            
