from django.contrib.auth.models import AbstractUser, User
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('owner', 'Owner'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='owner')
    image = models.ImageField(upload_to='profile/', default='../static/images/bot.jpg')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.username

    
    
