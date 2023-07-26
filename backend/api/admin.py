from django.contrib import admin
from .models import Game, Profile
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "score", "start_time", "end_time")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "score")


admin.site.register(Game, GameAdmin)
admin.site.register(Profile, ProfileAdmin)