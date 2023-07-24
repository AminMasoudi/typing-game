from django.urls import path

from . import views

# my urls
urlpatterns = [
    path("register", views.register, name="register"),
]
