
from django.urls import path,include
from .import views
app_name='registration'
urlpatterns = [

    path('index/',views.index,name='index'),
    path('registration/',views.RegistrationApi.as_view(),name='registration'),
    path('registration/<int:pk>/',views.RegistrationApi.as_view(),name='registration'),
    path('bussiness/',views.BussinessApi.as_view(),name='registration'),
    path('bussiness/<int:pk>/',views.BussinessApi.as_view(),name='registration'),
    path('admission/',views.AdmissionApi.as_view(),name='admission'),
    path('admission/<int:pk>/',views.AdmissionApi.as_view(),name='admission'),

    # path('reference/',views.referenceApi.as_view(),name='reference'),
    path('relation/',views.RelationApi.as_view(),name='relation'),
    path('relation/<int:pk>/',views.RelationApi.as_view(),name='relation'),
    path('documents/',views.DocumentApi.as_view(),name='documents'),
    path('documents/<int:pk>/',views.DocumentApi.as_view(),name='documents'),
    # path('email/',views.EmailWork.as_view(),name='email'),
    path('sorting/',views.SortingData.as_view(),name='sorting'),

    path('registrationclass/',views.RegistationCreate.as_view(),name='registrationclass'),
    path('registrationbusiness/',views.RegistrationBusiness.as_view(),name='registrationbusiness/'),
    path('registrationstudentstatus/',views.StudentStatusDetail.as_view(),name='registrationstudentstatus'),
    path('studenteducation/',views.StudentEducationDetail.as_view(),name='studenteducation'),
    path('studentenew/',views.StudentNew.as_view(),name='studentenew'),
    path('studentrelative/',views.StudentRelative.as_view(),name='studentrelative'),
    path('studentdocument/',views.StudentDocument.as_view(),name='studentdocument'),
    path('pdf',views.some_view,name='pdf'),

    path('try/',views.try1,name='try')



]