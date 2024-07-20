from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, authenticate
from .serializer import UserSerializer,UsuarioSerializer
from rest_framework import generics
import json
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

#class ApiView(generics.ListCreateAPIView):
class ApiView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

#@api_view(['POST'])
def Register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def Login(request):
    serializer_class = UsuarioSerializer
    email = request.data.get('email')
    password = request.data.get('password')
    print(f"Email: {email}, Password: {password}")

    try:
        user = User.objects.get(email=email)
        print(f"Usuario encontrado: {user}")
    except User.DoesNotExist:
        print("Usuario no encontrado")
        return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

    print("Resultado de authenticate 1:", user)
    user = authenticate(request, email=email, password=password)
    print("Resultado de authenticate 2:", user)

    if user is not None:
        return Response({'message': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

#def get(self, request, *args, **kwargs):
#    serializer
#  = UserSerializer(User.objects.all(), many=True)
#    return Response(serializer.data, status=status.HTTP_200_OK)