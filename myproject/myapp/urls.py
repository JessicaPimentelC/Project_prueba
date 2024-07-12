from django.urls import path
from myapp.views import register, login

urlpatterns = [
    path('register/', register),
    path('login/', login),
]