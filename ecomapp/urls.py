from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter 

router=DefaultRouter()
router.register('users',UserView)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',obtain_auth_token)
]
