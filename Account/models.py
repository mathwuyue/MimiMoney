from django.db import models
from django.contrib.auth.models import User
from money.Utils.constants import STATE
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User) #ForeignKey(Usr, unique = True)
    homeaddr = models.CharField(max_length=30, blank=True, default='')
    state = models.CharField(max_length=3, choices=STATE,blank=True)
    country = models.CharField(max_length=20,blank=True)
    contact = models.CharField(max_length=16,blank=True)
