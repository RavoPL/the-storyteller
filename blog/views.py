from django.shortcuts import render, HttpResponse

# Create your views here.

blogposts = [
    {
        'author': 'Dorian',
        'title': 'Lord of the Rings',
        'description': 'There and Back Again',
        'date_posted': 'May 23rd, 2023',
    },
    {
        'author': 'Jack',
        'title': 'Harry Potter',
        'description': 'Youre a Wizard',
        'date_posted': 'May 22nd, 2023',
    },
    {
        'author': 'Mary',
        'title': 'Lovecraft',
        'description': 'Cosmic Horror',
        'date_posted': 'May 10th, 2023',
    },
]

def homepage(request):
    context = {
        'blogposts': blogposts
    }
    return render(request, "blog/homepage.html", context)

def aboutpage(request):
    return render(request, "blog/aboutpage.html", {'title': 'About Page'})