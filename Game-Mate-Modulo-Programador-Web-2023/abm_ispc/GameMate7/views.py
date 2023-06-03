from django.shortcuts import render

from django.contrib.auth import authenticate, login
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import Registro, Login, CustomUser
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializers import LoginUsuarioSerializer
from .serializers import RegistroUsuarioSerializer
from rest_framework import viewsets
#from rest_framework import generics, permissions, status
#from rest_framework.response import Response
#from rest_framework_simplejwt.tokens import RefreshToken
#from GameMate7.serializers import RegistroUsuarioSerializer, LoginUsuarioSerializer
#from django.http import HttpResponse

# Create your views here.

class RegistroUsuarioView(APIView):
    permission_classes = (AllowAny)

class LoginUsuarioView(APIView):
    permission_classes = (AllowAny)

    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)
        