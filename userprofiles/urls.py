from django.urls import path 
from .views import * 

urlpatterns = [
    path("", profilePage, name="profile")
]