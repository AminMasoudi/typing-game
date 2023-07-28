from django.contrib.auth.models import User

from rest_framework import serializers

from api.models import Game, Profile



class GameSerializers(serializers.ModelSerializer):
    score = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Game
        fields = ("id", "score", "username")
        depth = 1

    def get_user(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            return user
        else :
            raise serializers.ValidationError("user not found", 403)
    def get_score(self, obj):
        return obj.score
            

    def create(self, validated_data):
        user = self.get_user()
        if not user.games.filter(end_time=None):
            game = Game.objects.create(user=user,
                                       score = 0)
            return game
        raise serializers.ValidationError("not complete game exist")




class RegisterSerializer(serializers.Serializer):
    username    = serializers.CharField(min_length=5)
    password    = serializers.CharField(min_length=8)
    password2   = serializers.CharField(min_length=8)

    def create(self, validated_data):
        
        username = validated_data.get("username")
        password = validated_data.get("password")
        user = User.objects.create_user(username, password=password)
        if user:
            prof = Profile.objects.create(user=user, score=0)
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
    



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user", "score", "username"]
        
