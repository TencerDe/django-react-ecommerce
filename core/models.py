from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate

# Create your models here.

class CustomUser(AbstractUser):
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username
