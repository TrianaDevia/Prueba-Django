from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Registro, Login,  CustomUser
from django.contrib.auth.hashers import make_password

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password')
    def validate_password(self, value):
        return make_password(value)

class LoginUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email',  'password')
    def validate_password(self, value):
        return make_password(value)

