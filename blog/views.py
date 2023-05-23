from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("<h1>TEST MAIN PAGE</h1>")

def aboutpage(request):
    return HttpResponse("<h2>TEST ABOUT PAGE<h2>")