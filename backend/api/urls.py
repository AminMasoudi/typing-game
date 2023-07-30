from django.urls import path
from django.views.generic import TemplateView

from .views import auth, game, general


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Swagger ui for speed typing game API's",
      contact=openapi.Contact(email="aminmasoudi2003+jobs@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# my urls
urlpatterns = [
    path(r"auth/register/", auth.RegisterView.as_view(), name="register"),
    path(r"auth/login/", auth.LoginView.as_view(), name="login"),

    path(r"game/", game.GameListCreate.as_view(), name="game"),

    path("seq/", game.SeqAPIView.as_view(), name="seq"),
    
    path(r"leaders/", general.LeadersAPI.as_view(), name="leaders"),
    path(r"progress/", general.ProgressAPI.as_view(), name="progress"),


   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path("schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    # path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

