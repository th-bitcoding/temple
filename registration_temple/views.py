import datetime
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
from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
# Create your views here.
def index(request):
    return HttpResponse('hello django')

def username_check(request):
    username = request.data.get('username')
    check_data = Registration.objects.get(username=username)
    print('4545',check_data)
    return check_data

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
            subject = 'Username and Password'
            message = f'Hello How are you!!! your Username is :{username} and your password is : {password}'
            from_email = settings.EMAIL_HOST_PASSWORD
            recipient_list = [email]
            send_mail(subject,message,from_email,recipient_list)
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
    
    def getuserreference(self,pk):
        try:
            return Admissionreference.objects.get(pk=pk)
        except Admissionreference.DoesNotExist:
            return None
    
    def get(self,request,*args,**kwargs):
        flag=request.query_params.get('flag')
        print('flag',flag.lower())
        if flag.lower() == "yes":
            queryset =Admission.objects.all()
            serializer = AdmissionSerializers(queryset,many=True)
            return Response(serializer.data)
        else:
            queryset =Admissionreference.objects.all()
            serializer = AdmissionreferenceSerializers(queryset,many=True)
            return Response(serializer.data)
        
    def post(self,request):
        flag=request.query_params.get('flag')

        if flag.lower() == "yes":
            serializers = AdmissionSerializers(data=request.data)
        else:
            serializers = AdmissionreferenceSerializers(data=request.data)

        if serializers.is_valid():
            username = request.data.get('username')
            check_username = Registration.objects.get(username=username)
            serializers.save(username=check_username)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

        
    def put(self, request, pk):
            flag = request.query_params.get('flag')

            if flag.lower() == "yes":
                snippet = self.getuser(pk)
                serializers = AdmissionSerializers(snippet, data=request.data)
            else:
                snippet = self.getuserreference(pk)
                serializers = AdmissionreferenceSerializers(snippet, data=request.data)

            if serializers.is_valid():
                username=request.data.get('username')
                try:
                    check_username = Registration.objects.get(username=username)
                except Registration.DoesNotExist:
                    return Response({'Message':'Username Does Not Exist'})
                serializers.save(username=check_username)
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request,*args,**kwargs):
        new = self.kwargs['pk']
        flag = request.query_params.get('flag')

        if flag.lower() == "yes":
            snippet = self.getuser(new)
        else:
            snippet = self.getuserreference(new)

        snippet.delete()
        return Response({'message':'Delete Successfully'},status=status.HTTP_204_NO_CONTENT)



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
            username = request.data.get('username')
            get_username = Registration.objects.get(username=username)
            serializers.save(username=get_username)
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        snippet = self.getuser(pk)
        serializers = RelationSerializers(snippet,data=request.data)
        if serializers.is_valid():
            username = request.data.get('username')
            try:
                get_username = Registration.objects.get(username=username)
            except Registration.DoesNotExist:
                return Response({'Message':'Username Does Not Found'})
            serializers.save(username=get_username)
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
            try:
                get_username = Registration.objects.get(username=username)
            except Registration.DoesNotExist:
                return Response({'Message':'Username Does Not Found'})
            serializers.save(username = get_username)
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
    

class EmailWork(APIView):
    def get_queryset(self):
        return EmailCheckModel.objects.all()
    
    def get(self,request,*args,**kwargs):
        current_date=datetime.date.today()
        check = EmailCheckModel.objects.get(DOB =current_date)
        name = check.name
        email = check.email
        subject = 'Birthday Wish'
        message = f'Happy Birthday :{name} Have a Great Day'
        from_email = settings.EMAIL_HOST_PASSWORD
        recipient_list = [email]
        send_mail(subject,message,from_email,recipient_list)
        queryset = self.get_queryset()
        serializers = EmailWorkSerializers(queryset,many=True)
        return Response(serializers.data)
    




    
    
    

            
