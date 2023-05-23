from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return render(request, "blog/homepage.html")

def aboutpage(request):
    return HttpResponse("<h2>TEST ABOUT PAGE<h2>")