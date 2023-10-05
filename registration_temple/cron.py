import datetime
import random
import logging  # Import the logging module
from logging.handlers import RotatingFileHandler  # Import the RotatingFileHandler
from .models import *
from .views import *
from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail
from .serializers import *
from rest_framework.response import Response


logging.basicConfig(filename="/home/bitcoding/Documents/github/temple/temple/registration_temple/cron.log", level=logging.INFO)

def cron_handle():
    logging.info("Starting cron_handle function")
    emailwork = BirthdayEmail()
    info_response = emailwork.get(None)
    logging.info(info_response.status_code)
    logging.info("Finished cron_handle function")
    return True
