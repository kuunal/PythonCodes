# from .models import RegisterModel
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from ParkingLot import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


def send_verification(user_email, subject="Account created successfully", host=settings.HOST):
    user = User.objects.filter(email=user_email)
    subject = subject
    message = "Thank you! Your account has been created. Please click on the link below to start things up."
    html_message = render_to_string('register/activate.html',{
        'user_name' : user.values_list('username', flat=True),
        'uid' : urlsafe_base64_encode(force_bytes(user.values_list('id', flat=True))),
        'email': urlsafe_base64_encode(force_bytes(user_email)),
        'host': host
    })
    from_email = settings.EMAIL_HOST_USER
    to_list = [user_email,]
    send_mail(subject, message, from_email, to_list, html_message=html_message)
