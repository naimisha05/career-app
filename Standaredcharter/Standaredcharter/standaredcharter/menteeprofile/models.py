import email
from pyexpat import model
from django.db import models

# Create your models here.
class Menteeprofile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    interest = models.TextField(max_length=300)
    choosen_Course = models.TextField(max_length=300)
    qualification = models.TextField(max_length=300)
    experience = models.TextField(max_length=300)
    achivements = models.TextField(max_length=300)
    contact = models.IntegerField()