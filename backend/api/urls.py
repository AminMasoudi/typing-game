from django.urls import path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

from .views import auth, game, general
from . import view



schema = get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0",
)


# my urls
urlpatterns = [
    path(r"auth/register/", auth.RegisterView.as_view(), name="register"),
    path(r"auth/login/", auth.LoginView.as_view(), name="login"),

    path(r"game/", game.GameListCreate.as_view(), name="game"),

    path("seq/", game.SeqAPIView.as_view(), name="seq"),
    
    path(r"leaders/", general.LeadersAPI.as_view(), name="leaders"),
    path(r"progress/", general.ProgressAPI.as_view(), name="progress"),


    path('openapi', schema, name='openapi-schema'),
    
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),


    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    # path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

