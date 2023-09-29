from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import *
# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer