from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Profile
from api.serializers import UserProfileSerializer, GameSerializers

class LeadersAPI(APIView):
    def get(self, request, *args, **kwargs):
        leaders = Profile.objects.all().order_by("score").reverse()[0:10]
        leaders = UserProfileSerializer(leaders, many=True)
        return Response(leaders.data)
    

class ProgressAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
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
        
