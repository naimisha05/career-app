from django.urls import path

from . import views

urlpatterns = [
    path("mentorprofile", views.mentorprofile, name="mentorprofile")
]