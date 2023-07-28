from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.timezone import now
from .serializers import GameSerializers
# from.serializers.models import UserProfileSerializer, UserSerializer, GameSerializer
from .models import  Game, Profile
from . import util
import time

# Create your views here.




@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def new_game(request):
    if "game" not in request.session:
        request.session["game"] = {}

    game = Game.objects.create(
        user=request.user,
        score = 0,
    )
    #TODO use redis
    game_session = {
        "id" : game.pk,
        "user" : request.user.pk,
        "start_time" : game.start_time.__str__(),
        "score" : game.score,
        
    }
    
    request.session["game"] = game_session
    return Response({"game":game.pk})



@api_view(["GET"])
def cache(request):
    return Response(request.session)



#TODO write a decorator to check if req.session[game] exist
@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def new_seq(request):
    game = request.session["game"]
    score = game["score"]
    seq, words = util.random(score+1)
    game["seq"] = seq
    request.session["game"] = game
    return Response({
        "words" : words,
        "seq" : seq
    })




#TODO clean this mess
@api_view(["PUT"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def calculate(request):
    try:
        game = Game.objects.get(pk=request.session["game"]["id"])
    except:
        pass #TODO
    seq = request.data["seq"]
    or_seq = request.session["game"]["seq"]
    score = util.calculate(seq, or_seq)
    request.session["game"]["score"] = request.session["game"]["score"] + score
    request.session["game"] = session_setter(score, game_session=request.session["game"])
    game.score = request.session["game"]["score"]
    game.save()

    return Response({"AT" : "OK"})


def session_setter(score, **game_session):
    return game_session["game_session"]


@api_view(["PUT"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def update(request):
    game = Game.objects.get(pk=request.session["game"]["id"])
    game.score = request.session["game"]["score"]
    game.end_time = now()
    game.save()
    prof = request.user.profile
    prof.score += request.session["game"]["score"]
    prof.save()
    return Response({"AT" : "OK"})


@api_view(["GET"]) 
def leads(request):
    users_profile = Profile.objects.all().order_by("score").reverse()[0:10]
    users_profile = UserProfileSerializer(users_profile, many=True).data
    users_profile = list(map(lambda user: prety(user), users_profile))
    return Response(users_profile)


def prety(profile):
    user = User.objects.get(pk=profile["user"])
    user = UserSerializer(user)
    profile["user"] = user.data
    return profile

@api_view(["GET"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def progress(request):
    games = request.user.games.all()
    number_of_games = len(games)
    scores_list = list(map(lambda game:game.score, games))
    games = GameSerializers(games, many=True)
    max_score = max(scores_list)
    av = sum(scores_list) / number_of_games
    return Response({
        "best_record" : max_score,
        "average" : av,
        "total"   : number_of_games,
        "games" : games.data
    })
    
