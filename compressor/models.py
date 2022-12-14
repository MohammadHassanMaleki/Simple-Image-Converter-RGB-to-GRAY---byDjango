from sre_parse import Verbose
from tabnanny import verbose
from django.db import models



class Images(models.Model): 
    id = models.AutoField(primary_key=True)
    original_img = models.ImageField(upload_to='original/', null=True, verbose_name= 'تصویر اصلی') 
    original_size = models.TextField(null=True)
    quality = models.CharField(max_length=3, null=True, verbose_name='کیفیت')
    converted_img = models.ImageField(upload_to='converted/', null=True) 
    converted_size = models.TextField(null=True)

    