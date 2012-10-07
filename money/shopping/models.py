# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ShoppingData(models.Model):
    _SHOPPING_TYPE = (
        ('FOOD', '食物'),
        ('BOOK', '书'),
        ('FURNITURE', '家俱'),
        ('LIFEUSE', '生活用品'),
        ('ELE', '电子产品'),
        ('CAR', '车以及车用品'),
        ('TRANS', '路费'),
        ('TRAVEL', '旅游用费'),
        ('RESTURANT', '餐馆吃饭'),
        ('OTHER', '其他')
        )

    user = models.ForeignKey(User, related_name='+')  

    title = models.CharField(max_length=60)
    price = models.FloatField()
    currency = models.CharField(max_length=3, default='GBP')
    shopping_type = models.CharField(max_length=12, choices=_SHOPPING_TYPE, default='OTHER')
    paying_type = models.CharField(max_length=30, default='Cash')
    shop_name = models.CharField(max_length=16,blank=True)
    place = models.TextField(blank=True)
    date = models.DateField(auto_now=True,auto_now_add=True)
    description = models.TextField(blank=True)
    rank = models.IntegerField(blank=True)
