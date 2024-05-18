from django.db import models

class Event(models.Model):
    game = models.IntegerField()
    description = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.IntegerField()
