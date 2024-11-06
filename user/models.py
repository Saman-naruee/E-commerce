from django.db import models
from django.contrib import admin
from django.conf  import settings
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

class UserProfile(models.Model):
    class Membership(models.TextChoices):
        BRONZE = 'B', 'Bronze'
        SILVER = 'S', 'Silver'
        GOLD = 'G', 'Gold'

    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=Membership, default=Membership.BRONZE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    def __str__(self) -> str:
        return f"Mr.{self.user.last_name}"
    
    class Meta:
        permissions = [
            ('view_history', 'Can View History')
        ]


class Notification(models.Model):
    READING_STATUS = [
        ('R', 'Readed'), 
        ('U', 'Unread')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    send_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=READING_STATUS, default='Unread')

    def __str__(self) -> str:
        return f'{self.message} - {self.user.username}'
