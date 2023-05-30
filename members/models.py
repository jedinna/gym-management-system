from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_gymuser = models.BooleanField('Is gymuser', default=False)
    is_coach = models.BooleanField('is coach', default=False)