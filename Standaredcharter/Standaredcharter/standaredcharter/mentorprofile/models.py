import email
from pyexpat import model
from django.db import models

# Create your models here.
class Mentorprofile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.TextField(max_length=300)
    spicility = models.TextField(max_length=300)
    knowledge = models.TextField(max_length=300)
    experience = models.TextField(max_length=300)
    achivements = models.TextField(max_length=300)
    projects = models.TextField(max_length=300)
    contact = models.IntegerField()