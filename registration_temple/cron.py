
import datetime
import random
from .models import *
from rest_framework.views import APIView


current_data = datetime.date.today()

class EmailWork(APIView):
    def get(self,request,*args,**kwargs):
      current_data = datetime.date.today()
      print('current date',current_data)
      check_data = EmailCheck.objects.get(DOB = current_data)
      print('4545',check_data)
  