from django.urls import path,include
from .views import ApiView, Login
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', ApiView, basename='UserManager')
#router.register('api', Login, basename='Login')

    
#urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)), 
    path('register/', views.Register, name='register'),    
    path('login/', views.Login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),

]