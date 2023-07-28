from django.urls import path
from .views import auth
from . import view

# my urls
urlpatterns = [
    path(r"auth/register/", auth.RegisterView.as_view(), name="register"),
    path(r"auth/login/", auth.LoginView.as_view(), name="login"),

    path("new_game/", view.new_game, name="new_game"),
    path("cache/", view.cache),
    path("new_seq/", view.new_seq, name="new_seq"),
    path("calculate", view.calculate, name="calculate"),
    path("update/", view.update, name="update"),
    path("leaders/", view.leads, name="leaders"),
    path("progress/", view.progress, name="progress"),
]
