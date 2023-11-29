from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    # path('about/', views.aboutpage, name="storyteller-aboutpage"),
    # path('contact/', views.contactpage, name="storyteller-contactpage"),
]