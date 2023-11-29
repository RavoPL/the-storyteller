from django.shortcuts import render, HttpResponse, get_object_or_404
# from . import models
from .models import Post
from django.views import generic, View

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )

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