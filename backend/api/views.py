from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .serializers.requests import LoginSerializer, RegisterSerializer
from .models import  Game
# Create your views here.


@api_view(["POST"])
def register(request):
    register_ser = RegisterSerializer(data=request.data)
    if register_ser.is_valid(raise_exception=True):
        user = register_ser.save()
        login(request ,user)

        return Response(register_ser.validated_data)



@api_view(["POST"])
def log_in(request):
    login_ser = LoginSerializer(User, data=request.data)
    login_ser.is_valid(raise_exception=True)
    user = authenticate(request, username=login_ser.validated_data.get("username"), password=login_ser.validated_data.get("password"))
    if user:
        login(request, user)
        return Response(login_ser.validated_data)
    return Response({
        "error": "failed to log in"
    })



@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def new_game(request):
    if "game" not in request.session:
        request.session["game"] = []

    game = Game.objects.create(
        user=request.user,
        score = 0,
    )
    #TODO use redis
    game_session = {
        "id" : game.pk,
        "user" : request.user.pk,
        "start_time" : game.start_time.minute,
        "score" : game.score,
        "end_time" : game.end_time
    }
    
    request.session["game"] +=  [game_session]
    return Response({"game":game.pk})
