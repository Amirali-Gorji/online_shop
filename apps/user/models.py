from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)


class OTPCode(models.Model):
    PHONE_NUMBER = 0
    EMAIL = 1
    OTP_TYPES = (
        (PHONE_NUMBER, 'Phone_number'),
        (EMAIL, 'Email'),
    )
    type = models.IntegerField(choices=OTP_TYPES)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    token = models.CharField(max_length=10)

    



