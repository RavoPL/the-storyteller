from django.shortcuts import render, HttpResponse
# from . import models
from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

# def homepage(request):
#     blogposts = models.Blogpost.objects.all()
#     context = {
#         'blogposts': blogposts
#     }
#     return render(request, "blog/homepage.html", context)

# def aboutpage(request):
#     return render(request, "blog/aboutpage.html", {'title': 'About Page'})

# def contactpage(request):
#     return render(request, "blog/contactpage.html", {'title': 'Contact Page'})