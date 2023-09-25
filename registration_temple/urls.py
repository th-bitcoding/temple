
from django.urls import path,include
from .import views
urlpatterns = [

    path('',views.index,name='index'),
    path('registration/',views.RegistrationApi.as_view(),name='registration'),
    path('bussiness/',views.BussinessApi.as_view(),name='registration'),
    path('admission/',views.AdmissionApi.as_view(),name='admission'),
    path('reference/',views.referenceApi.as_view(),name='reference'),
    path('relation/',views.RelationApi.as_view(),name='relation'),
    path('documents/',views.DocumentApi.as_view(),name='documents'),


]