from api.models import Game, Profile
from django.contrib.auth.models import User

from rest_framework import serializers
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['pk', 'score', ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "score"]
        
