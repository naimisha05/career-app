from django.shortcuts import render

from menteeprofile.models import Menteeprofile

def menteeprofile(request):
    #menteeprofile = Menteeprofile.objects.all()
    return render(request, "profile.html")