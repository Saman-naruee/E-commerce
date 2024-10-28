from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(validators=[RegexValidator(
        regex=r'^(\+98|0)\d{10}$',
        message='Phone number must start with +98 and be 13 digits long, or start with 0 and be 11 digits long'
    )], max_length=13)

    groups = models.ManyToManyField(  
        Group,  
        related_name='custom_user_set',  # Change if needed  
        blank=True,  
        help_text=('The groups this user belongs to. A user will get all permissions '  
                    'granted to each of their groups.'),  
        verbose_name='groups',  
    )  

    user_permissions = models.ManyToManyField(  
        Permission,  
        related_name='custom_user_permissions',  # Change if needed  
        blank=True,  
        help_text='Specific permissions for this user.',  
        verbose_name='user permissions',  
    ) 