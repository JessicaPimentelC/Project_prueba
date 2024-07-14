from django.urls import path,include
from myapp.views import register, login
from .views import ApiView
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('api',ApiView.as_view(),basename='UserManager')
    
urlpatterns = [
    path('api/', include(router.urls)), 
    path('register/', ApiView.post, name='register'),    
    path('login/', ApiView.post, name='login'),]