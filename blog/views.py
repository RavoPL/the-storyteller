from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def homepage(request):
    blogposts = models.Blogpost.objects.all()
    context = {
        'blogposts': blogposts
    }
    return render(request, "blog/homepage.html", context)

def aboutpage(request):
    return render(request, "blog/aboutpage.html", {'title': 'About Page'})

def contactpage(request):
    return render(request, "blog/contactpage.html", {'title': 'Contact Page'})