import datetime
import random
import string
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from .models import *
from rest_framework.exceptions import APIException
from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.views.generic import View
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def index(request):

    return HttpResponse("Thank You")

def try1(request,):
    print('4545',request.GET.get('email'))
    data = Registration.objects.get(email=request.GET.get('email'))
    main_data = {
        "data":data
    }
    return render(request,'xyz.html',main_data)


class RegistationCreate(CreateView):
    permission_classes = (AllowAny,)
    model = Registration
    form_class = RegistrationForm
    template_name = 'registration.html'
    # success_url =reverse_lazy(f'registration:try')

    def form_valid(self, form):

        get_secondary_country = form.cleaned_data['secondary_country']
        get_secondary_phone = form.cleaned_data['secondary_phone']
        get_other_country = form.cleaned_data['other_country']
        get_other_phone = form.cleaned_data['other_phone']
        get_DOB = form.cleaned_data['DOB']

        get_marriage_date = form.cleaned_data['marriage_date']
        get_first_name = form.cleaned_data['first_name']
        get_middle_name = form.cleaned_data['middle_name']
        get_last_name = form.cleaned_data['last_name']
        get_grand_father_name = form.cleaned_data['grand_father_name']

        get_email = form.cleaned_data['email']
        get_secondary_email = form.cleaned_data['secondary_email']

        check_email = Registration.objects.filter(email=get_email).exists()
        if get_secondary_email =='':
            pass
        else:
            check_secondary_email = Registration.objects.filter(secondary_email=get_secondary_email)

            if check_secondary_email.exists():
                messages.warning(self.request, "Seconday Email already exists.")
                form.add_error('secondary_email', 'Secondary Email already exists.') 
                return self.render_to_response(self.get_context_data(form=form))

        if get_secondary_country and not get_secondary_phone:
            messages.warning(self.request, "Enter Secondary Phone Number")
            form.add_error('secondary_phone', 'Enter Secondary Phone Number.') 
            return self.render_to_response(self.get_context_data(form=form))
        
        if get_secondary_phone and not get_secondary_country:
            messages.warning(self.request, "Please select Seconday Country")
            form.add_error('secondary_country', 'Please select Seconday Country.') 
            return self.render_to_response(self.get_context_data(form=form))
        
        if get_other_country and not get_other_phone:
            messages.warning(self.request, "Enter Other Phone Number")
            form.add_error('other_phone', 'Enter Other Phone Number.') 
            return self.render_to_response(self.get_context_data(form=form))
        
        
        if get_other_phone and not get_other_country:
            messages.warning(self.request, "Please select Other Country")
            form.add_error('other_country', 'Please select Other Country.') 
            return self.render_to_response(self.get_context_data(form=form))


        # if get_marriage_date == today_date:
        #     messages.warning(self.request, "select Valid Date.")
        #     form.add_error('marriage_date', 'Select Valid Date.') 
        #     return self.render_to_response(self.get_context_data(form=form))
        
        if get_email == get_secondary_email:
            messages.warning(self.request, "Both Email Are Same.")
            form.add_error('secondary_email', 'Both Email Are Same.') 
            form.add_error('email', 'Both Email Are Same.') 
            return self.render_to_response(self.get_context_data(form=form))
        
        # if get_primary_country =='' or get_primary_phone =='':
        #     messages.warning(self.request, "Both Email Are Same.")
        #     form.add_error('primary_country', 'Both Email Are Same.') 
        #     form.add_error('primary_phone', 'Both Email Are Same.') 
        #     return self.render_to_response(self.get_context_data(form=form))
        
        if get_DOB is not None and get_marriage_date is not None:
   
            age_difference = (get_marriage_date - get_DOB).days
            if age_difference < 3650: 
                messages.warning(self.request, "Select a Valid Date.")
                form.add_error('marriage_date', 'Select a Valid Date.') 
                return self.render_to_response(self.get_context_data(form=form))


        if get_first_name:
            for data in get_first_name:
                if not data.isalpha():
                    messages.warning(self.request, "Only alphabetic characters are allowed in the first name.")
                    form.add_error('first_name', 'Only alphabets allowed')
                    return self.render_to_response(self.get_context_data(form=form))
                
        if get_middle_name:
            for data in get_middle_name:
                if not data.isalpha():
                    messages.warning(self.request, "Only alphabetic characters are allowed in the middle name.")
                    form.add_error('middle_name', 'Only alphabets allowed')
                    return self.render_to_response(self.get_context_data(form=form))
                
        if get_last_name:
            for data in get_last_name:
                if not data.isalpha():
                    messages.warning(self.request, "Only alphabetic characters are allowed in the last name.")
                    form.add_error('last_name', 'Only alphabets allowed')
                    return self.render_to_response(self.get_context_data(form=form))
                
        if get_grand_father_name:
            for data in get_grand_father_name:
                if not data.isalpha():
                    messages.warning(self.request, "Only alphabetic characters are allowed in the Grand Father Name.")
                    form.add_error('grand_father_name', 'Only alphabets allowed')
                    return self.render_to_response(self.get_context_data(form=form))


        if check_email:
            messages.warning(self.request, "Email already exists.")
            form.add_error('email', 'Email already exists.') 
            return self.render_to_response(self.get_context_data(form=form))

        form.save()
        success_url = reverse_lazy('registration:registrationbusiness/') + f'?email={get_email}'
        messages.success(self.request, "Data has been successfully inserted.")
        return HttpResponseRedirect(success_url)
    
class RegistrationBusiness(CreateView):
    permisson_classes = (AllowAny,)
    model = Business
    form_class = RegistrationBusiness
    template_name = 'registration_business.html'

    def form_valid(self, form):
        email = self.request.GET.get('email')
        try:
            student_email = Registration.objects.get(email=email)

            form.instance.registration = student_email
            form.save()

            success_url = reverse_lazy('registration:registrationstudentstatus') + f'?email={email}'
            messages.success(self.request, "Data has been successfully inserted.")
            return HttpResponseRedirect(success_url)

        except Registration.DoesNotExist:
           
            raise ValueError("No Registration found with the provided email.")
  
class StudentStatusDetail(CreateView):
    permisson_classes = (AllowAny,)
    model = StudentStatus
    form_class = StudentStatusForm
    template_name = "student_status.html"

    def form_valid(self,form):
        email = self.request.GET.get('email')
        
        try:
            student_email = Registration.objects.get(email=email)
            print('student_email',student_email)
            form.instance.student = student_email
            form.save()
            check_status = StudentStatus.objects.get(student = student_email)
            if check_status.student_status == "Yes":
                success_url = reverse_lazy('registration:studenteducation') + f'?email={email}'
            else:
                success_url = reverse_lazy('registration:studentenew') + f'?email={email}'
            messages.success(self.request, "Data has been successfully inserted.")
            return HttpResponseRedirect(success_url)
        except Registration.DoesNotExist:

            raise ValueError("No Registration found with the provided email.")
        
class StudentEducationDetail(CreateView):
    permission_classes = (AllowAny,)
    model = EducationDetail
    form_class = StudentEducationForm
    template_name = "education_detail.html"

    def form_valid(self,form):
        email = self.request.GET.get('email')
        print('email44',email)
        try:
            student_email = Registration.objects.get(email=email)
            form.instance.student = student_email
            form.save()
            success_url = reverse_lazy('registration:studentrelative') + f'?email={email}'
            messages.success(self.request, "Data has been successfully inserted.")
            return HttpResponseRedirect(success_url)
        except Registration.DoesNotExist:
            raise ValueError("No Registration found with provided email")
        
class StudentNew(CreateView):
    permission_classes = (AllowAny,)
    model = Admissionreference
    form_class = StudentNewForm
    template_name = "studentnew.html"

    def form_valid(self,form):
        email = self.request.GET.get('email')
        try:
            student_email =Registration.objects.get(email=email)
            form.instance.student =student_email
            form.save()
            success_url = reverse_lazy('registration:studentrelative') + f'?email={email}'
            return HttpResponseRedirect(success_url)
        except Registration.DoesNotExist:
            raise ValueError("No registration found with provided email")
        
class StudentRelative(CreateView):
    permission_classes=(AllowAny,)
    model = Student_Relative
    form_class = StudentRelationForm
    template_name="student_relative.html"

    def form_valid(self,form):
        email = self.request.GET.get('email')
        try:
            student_email = Registration.objects.get(email=email)
            form.instance.student = student_email
            form.save()
            success_url = reverse_lazy('registration:studentdocument') + f'?email={email}'

            return HttpResponseRedirect(success_url)
        except Registration.DoesNotExist:
            raise ValueError("No registration found with provided email")
        
class StudentDocument(CreateView):
    permission_classes = (AllowAny,)
    model = Document
    form_class = StudentDocumentForm
    template_name = "student_documents.html"

    def form_valid(self,form):
        email = self.request.GET.get('email')
        print('email',email)
        try:
            student_email=Registration.objects.get(email=email)
            form.instance.studentdocument = student_email
            form.save()
            success_url = reverse_lazy('registration:index')

            return HttpResponseRedirect(success_url)
        except Registration.DoesNotExist:
            raise ValueError("No Registration FOund With Provided email")

def some_view(request):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Query the Registration object
    data = Registration.objects.get(id=2)


    table_data = [
        ['First Name','middle_name' 'Last Name','primary_country','primary_phone'],
        [data.first_name, data.middle_name,data.last_name],
    ]

    table = Table(table_data)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)

    elements = []
    elements.append(table)
    doc.build(elements)

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")
    
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
    

class BirthdayEmail(APIView):
    def get_queryset(self):
        return Registration.objects.all()
    
    def get(self, request, *args, **kwargs):
        current_date = datetime.date.today()

        checks = Registration.objects.filter(DOB=current_date)

        for check in checks:
            name = check.first_name
            email = check.email
            subject = 'Birthday Wish'
            message = f'Happy Birthday, {name}! Have a Great Day.'
            from_email = settings.EMAIL_HOST_USER 
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
        
        queryset = self.get_queryset()
        serializers = Registration(queryset)
        return Response(serializers)
    

    

class SortingData(APIView):

    def get_queryset(self):
        return Business.objects.all()
    
    def get(self,request,*args,**kwargs):
       
        city = request.query_params.get("city")
        city_data = Business.objects.filter(city_or_village=city)
        for data in city_data:
            Response_data={
                'username':data.username.username,
                'occupation':data.occupation,
                'education':data.education,
                'country':data.country,
                'city':data.city_or_village
            }
            return Response(Response_data)

    

    

    




    
    
    

            
