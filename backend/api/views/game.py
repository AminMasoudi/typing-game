from django.utils.timezone import now

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from api.serializers import GameSerializers
from api import util, schema

from rest_framework.exceptions import PermissionDenied


class GameListCreate(ListCreateAPIView):
    def get_queryset(self):
        return self.request.user.games.all()

    serializer_class = GameSerializers
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_description="PUT /game/ updates the current game", responses={200:GameSerializers(),
                                                                                                 403:openapi.Response("Forbidden"),
                                                                                                 404:openapi.Response("No incomplete game found")})
    def put(self, request, *args, **kwargs):
        if "seq" in request.session:
            del request.session["seq"]
            request.session.modified = True
        game = request.user.games.last()
        if game.end_time:
            return Response({"title": "game not found"},404)
        profile = request.user.profile
        game.end_time = now()
        profile.score += game.score
        game.save()
        profile.save()
        return Response({})
        



class SeqAPIView(APIView):

    permission_classes = [IsAuthenticated]
    
    @schema.seq_get
    def get(self, request, format=None, ):
        if "seq" in request.session:
            return Response({"detail":"seq exist"},400)
                
        game = request.user.games.last()
        score = game.score
        seq, words = util.random(score+1)
        request.session["seq"] = seq

        return Response({
            "words" : words,
            "seq" : seq
        })
    @schema.seq_post
    def post(self, request, format=None):
        if "seq" not in request.session:
            return Response({"detail": "seq session not set"},400)

        game = request.user.games.last()
        seq = request.data.get("seq")
        if not seq:
            return Response({"detail":"seq is required"},400)
        original_seq = request.session["seq"]

        score = util.calculate(seq, original_seq)
        del request.session["seq"]
        request.session.modified = True
        game.score += score
        game.save()
        return Response({"score":score})


