from pyexpat import model
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name= models.TextField(max_length=100)
    mentor_name = models.TextField(max_length=100)
    mentee_name = models.TextField(max_length=100)
    course_rating = models.IntegerField(max_length=2)
