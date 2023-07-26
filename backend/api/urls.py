from django.urls import path

from . import views

# my urls
urlpatterns = [
    path("register", views.register, name="register"),
    path("login", views.log_in, name="login"),
    path("new_game/", views.new_game, name="new_game"),
    path("cache/", views.cache),
    path("new_seq/", views.new_seq, name="new_seq")
]
