from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Registro, Login,  CustomUser
from django.contrib.auth.hashers import make_password

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    first_name = serializers.CharField(
        required=True)
    last_name = serializers.CharField(
        required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password')
    def validate_password(self, value):
        return make_password(value)

class LoginUsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    class Meta:
        model = get_user_model()
        fields = ('email',  'password')
    def validate_password(self, value):
        return make_password(value)

