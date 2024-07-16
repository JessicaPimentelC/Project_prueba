from django.urls import path,include
from .views import ApiView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', ApiView, basename='UserManager')
    
urlpatterns = router.urls

"""urlpatterns = [
    path('api/', include(router.urls)), 
    path('register/', views.register, name='register'),    
    path('login/', views.login, name='login'),]"""