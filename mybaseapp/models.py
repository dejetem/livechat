from django.db import models
from datetime import datetime

# Create your models here.

# room model
class RoomUsers(models.Model):
    name = models.CharField(max_length=1000)
    uid = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Message(models.Model):
    user_name = models.CharField(max_length=1000)
    room_name  = models.CharField(max_length=1000)
    text_value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user_name