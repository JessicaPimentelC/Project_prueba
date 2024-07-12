from django.urls import path
from myapp.views import register, login
from . import views
from rest_framework import routers


urlpatterns = [
    path('register/', views.register, name='register'),    
    path('login/', views.login, name='login'),]