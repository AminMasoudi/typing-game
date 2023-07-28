from django.urls import path
from .views import auth, game, general
from . import view

# my urls
urlpatterns = [
    path(r"auth/register/", auth.RegisterView.as_view(), name="register"),
    path(r"auth/login/", auth.LoginView.as_view(), name="login"),

    path(r"game/", game.GameListCreate.as_view(), name="game"),

    path("seq/", game.SeqAPIView.as_view(), name="seq"),
    
    path("leaders/", general.LeadersAPI.as_view(), name="leaders"),
    path("progress/", general.ProgressAPI.as_view(), name="progress"),
]
