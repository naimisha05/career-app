from django.shortcuts import render

def coursesone(request):
    return render(request, "course-1.html")

def coursestwo(request):
    return render(request, "course-2.html")

def coursesthree(request):
    return render(request, "course-3.html")