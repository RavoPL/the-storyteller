from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogpost(models.Model):
    # Sets the author of the blogpost and deletes all his content if account is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Sets the title of the blogpost
    title = models.CharField(max_length=100)
    # Sets the description of the blogpost
    description = models.TextField()
    # Sets the time and date of blogpost creation as well as blogpost update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)