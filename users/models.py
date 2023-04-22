from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    role_types = (
        ('normal_user','normal_user'),
        ('admin','admin'),
        ('artist','artist')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=role_types, default='normal_user')
    # other fields
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    # social = models.URLField(max_length=200, blank=True)
    image = models.ImageField(default='profile_images/default_profile.png',upload_to='profile_images/', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

