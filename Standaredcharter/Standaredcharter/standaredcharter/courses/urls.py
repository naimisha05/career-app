from django.urls import path

from . import views

urlpatterns = [
    path("course1", views.coursesone, name="courses1"),
    path("course2", views.coursestwo, name="courses2"),
    path("course3", views.coursesthree, name="courses3")
    
]