from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Blogpost(models.Model):
    # Sets the author of the blogpost and deletes all his content if account is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    # Sets the title of the blogpost
    title = models.CharField(max_length=200)
    # Sets the slug of the blogpost
    slug = models.SlugField(max_length=200, unique=True)
    # Sets the description of the blogpost
    description = models.TextField(blank=True)
    # Sets the content of the blogpost
    content = models.TextField()
    # Sets the time and date of blogpost creation as well as blogpost update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Sets the status of the post to either Draft or Published
    status = models.IntegerField(choices=STATUS, default=0)
    # Sets the likes on the blogpost
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")
    # Sets the name of the data models to their respective title
    def __str__(self):
        return self.title
    # Orders the blogposts according to the updated_at field
    class Meta:
        ordering = ['-updated_at']
    # Returns the total number of likes on a blogpost
    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    # Creates possibility of many comments and removes all comments if account is deleted
    post = models.ForeignKey(Blogpost, on_delete=models.CASCADE, related_name="comments")
    # Sets the author of the comment
    name = models.CharField(max_length=80)
    # Sets the e-mail of the account
    email = models.EmailField()
    # Sets the actual content of the comment box
    body = models.TextField()
    # Sets the time and date of when the comment was posted
    created_at = models.DateTimeField(auto_now_add=True)
    # Sets the default approval status of a comment as False
    approved = models.BooleanField(default=False)
    # Orders the comments according to the created_at field
    class Meta:
        ordering = ['created_at']
    # Displays the body of the comment and signs it with the name of the author
    def __str__(self):
        return f"Comment {self.body} by {self.name}"