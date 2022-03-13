from django.urls import path

from . import views

urlpatterns = [
    path("menteeprofile", views.menteeprofile, name="menteeprofile")
]