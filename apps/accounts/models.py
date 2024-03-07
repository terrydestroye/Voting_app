from django.db import models
from django.contrib.auth.models import AbstractUser


#Extension of built in User model
class CustomUser(AbstractUser):
    last_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return self.last_name + " " + self.first_name
    
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_groups',
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )









# Create your models here.
