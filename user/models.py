from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[RegexValidator(
        regex=r'^(\+98|0)\d{10}$',
        message='Phone number must start with +98 and be 13 digits long, or start with 0 and be 11 digits long'
    )], max_length=13)