from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.TextField()
    full_description = models.TextField()
    sender_phone_no = models.CharField(max_length=100)




class Project(models.Model):
    title = models.CharField(max_length=100)
    small_description = models.TextField()
    full_description = models.TextField()
    language = models.CharField(max_length=100)
    language_use = models.CharField(max_length=100)
    project_image = models.ImageField(upload_to='productimg')
    sample_img1 = models.ImageField(upload_to='productimg/sample')
    sample_img2 = models.ImageField(upload_to='productimg/sample')
    sample_img3 = models.ImageField(upload_to='productimg/sample')

    def __str__(self):
     return str(self.title)


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    post_img = models.ImageField(upload_to='productimg')

    def __str__(self):
     return str(self.id)
