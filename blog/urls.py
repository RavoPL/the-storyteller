from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="storyteller-homepage"),
    path('about/', views.aboutpage, name="storyteller-aboutpage"),
]