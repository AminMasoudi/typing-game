from django.utils.timezone import now

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from api.serializers import GameSerializers
from api import util




class GameListCreate(ListCreateAPIView):
    def get_queryset(self):
        return self.request.user.games.all()

    serializer_class = GameSerializers
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        if "seq" in request.session:
            del request.session["seq"]
            request.session.modified = True
        game = request.user.games.last()
        profile = request.user.profile
        game.end_time = now()
        profile.score += game.score
        game.save()
        profile.save()
        return Response({})
        



class SeqAPIView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, format=None, ):
        if "seq" in request.session:
            raise APIException("seq exist")
                
        game = request.user.games.last()
        score = game.score
        seq, words = util.random(score+1)
        request.session["seq"] = seq

        return Response({
            "words" : words,
            "seq" : seq
        })

    def post(self, request, format=None):
        if "seq" not in request.session:
            raise APIException("seq session not set")

        game = request.user.games.last()
        seq = request.data.get("seq")
        if not seq:
            raise APIException("seq is required")
        original_seq = request.session["seq"]

        score = util.calculate(seq, original_seq)
        del request.session["seq"]
        request.session.modified = True
        game.score += score
        game.save()
        return Response({"score":score})


