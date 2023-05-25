from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(models.Blogpost)
class BlogAdmin(SummernoteModelAdmin):
    # Automatically populates the slug field with the value in the title field
    prepopulated_fields = {'slug': ('title',)}
    # Allows the admin to filter through dates of post creation
    list_filter = ('status', 'created_at')
    # Displays the title, slug, status and date of creation of a post
    list_display = ('title', 'slug', 'status', 'created_at')
    # Allows the admin to search for posts by title or content
    search_fields = ['title', 'content']
    # Enables Summernote features in the content section
    summernote_fields = ('content')

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    # Allows the admin to filter through dates and approval status of comment creation
    list_filter = ('approved', 'created_at')
    # Displays the user name, body of comment, date of creation and approval status
    list_display = ('name', 'body', 'post', 'created_at', 'approved')
    # Allows the admin to search for comments by name, user e-mail or body of comment
    search_fields = ['name', 'email', 'body']