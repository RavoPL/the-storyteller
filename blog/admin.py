from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(models.Blogpost)
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')