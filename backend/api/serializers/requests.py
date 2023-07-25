from rest_framework import serializers
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class RegisterSerializer(serializers.Serializer):
    username    = serializers.CharField(min_length=5)
    password    = serializers.CharField(min_length=8)
    password2   = serializers.CharField(min_length=8)

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User.objects.create_user(username, password=password)
        if user:
            return user
        raise serializers.ValidationError("failed to auth")

    def validate_username(self, value):
        if User.objects.filter(username=value):
            raise serializers.ValidationError("username exist")
        return value

    def validate_password(self, value):
        #TODO password validation
        return value

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("passwords not match")
        return data