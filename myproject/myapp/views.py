from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model, authenticate
from .serializer import UserSerializer,UsuarioSerializer
from rest_framework import generics

User = get_user_model()

class ApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializerClass = UsuarioSerializer
    queryset=User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UsuarioSerializer(user, context=self.get_serializer_context()).data,
            "message": "User created successfully.",
        }, status=status.HTTP_201_CREATED)




#@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


def get(self, request, *args, **kwargs):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)