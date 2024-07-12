from django.urls import path
from myapp.views import register, login
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),    
    path('login/', views.login, name='login'),]