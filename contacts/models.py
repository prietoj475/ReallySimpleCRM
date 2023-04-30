from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, blank=False)
    last_name = models.CharField(max_length=15, blank=False)
    email = models.EmailField(blank=True)
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=47, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", null=True, default='static/nopic.png')
