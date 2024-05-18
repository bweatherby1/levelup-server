from django.db import models

class Game(models.Model):
  
    game_type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.IntegerField()
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
