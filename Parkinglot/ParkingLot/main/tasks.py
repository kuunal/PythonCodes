from __future__ import absolute_import, unicode_literals
from django.contrib.auth.models import User
from celery import shared_task
from register.send_mail import send_verification
from ParkingLot import settings
from django.core.mail import send_mail

MESSAGE_FOR_USER_VERIFICATION = "Please click on the link to start with the services"
MESSAGE_FOR_FORGOT_PASSWORD = "Click on the link to reset your password!"
MESSAGE_FOR_UNPARKING_VEHICLE = "Your vehicle has been unparked"
MESSAGE_FOR_LOT_IS_FULL = "Lot is Full"
MESSAGE_FOR_USER_VEHICLE_PARKED = "Your vehicle has been parked"

SUBJECT_FOR_USER_VERIFICATION = "Verify your account"
SUBJECT_FOR_FORGOT_PASSWORD = "Forgot password link"
SUBJECT_FOR_UNPARKING_VEHICLE = "Vehicle unparked"
SUBJECT_FOR_LOT_IS_FULL = "Parking Lot Full"
SUBJECT_FOR_USER_VEHICLE_PARKED = "Vehicle parked"



@shared_task
def send_mail_to_owner_when_lot_is_full(owner):
    owners = User.objects.filter().values_list('email', flat=True)
    for owner in owners:
        send_mail(SUBJECT_FOR_LOT_IS_FULL, MESSAGE_FOR_LOT_IS_FULL, settings.EMAIL_HOST_USER, [owner,])

@shared_task
def send_mail_to_user_when_vehicle_is_parked(user):
    send_mail(SUBJECT_FOR_USER_VEHICLE_PARKED, MESSAGE_FOR_USER_VEHICLE_PARKED, settings.EMAIL_HOST_USER, [user,])

@shared_task
def send_mail_to_user_when_vehicle_is_unparked(user, charges):
    message = f'Your vehicle has been unparked. Total charges are {charges}'
    send_mail(SUBJECT_FOR_UNPARKING_VEHICLE, message, settings.EMAIL_HOST_USER, [user,])

    
@shared_task
def send_verification_to_user(user):
    send_verification(user, SUBJECT_FOR_USER_VERIFICATION, MESSAGE_FOR_USER_VERIFICATION)

# @shared_task
# def send_reset