from django.shortcuts import render

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contact.html")

def blogs(request):
    return render(request, "blog.html")
