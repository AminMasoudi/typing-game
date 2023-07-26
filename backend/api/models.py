from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Game(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, related_name="games")
    start_time = models.TimeField(auto_now_add=True)
    score = models.IntegerField()
    end_time = models.TimeField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    score = models.IntegerField(default=0)
    