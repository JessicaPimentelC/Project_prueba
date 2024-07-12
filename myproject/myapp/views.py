from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.create_user(email=email, password=password)
    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

