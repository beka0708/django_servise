from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import re


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "role", "password", "confirm_password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if password != confirm_password:
            raise serializers.ValidationError({"password": "Пароли не совпадают."})

        if len(password) < 8:
            raise serializers.ValidationError(
                {"password": "Пароль должен быть не короче 8 символов."}
            )

        if not re.search(r"\d", password):
            raise serializers.ValidationError(
                {"password": "Пароль должен содержать хотя бы одну цифру."}
            )

        if not re.search(r"[A-Za-z]", password):
            raise serializers.ValidationError(
                {"password": "Пароль должен содержать хотя бы одну букву."}
            )

        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token
