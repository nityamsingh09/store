from django.db import models
import os
from django.conf import settings
from django.core.files import File
import subprocess

# Create your models here.
class Meme(models.Model):
   
    photo = models.ImageField(upload_to='photo/',blank=True, null=True)
    video = models.FileField(upload_to='video/',blank=True, null=True)
    title =models.TextField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    


class Giphy(models.Model):
   
    photo = models.ImageField(upload_to='photo/',blank=True, null=True)
    video = models.FileField(upload_to='video/',blank=True, null=True)
    title =models.TextField(max_length=100)
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
