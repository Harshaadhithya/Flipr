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

    def __str__(self):
        return self.user.email

