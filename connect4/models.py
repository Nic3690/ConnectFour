from django.db import models

class ConnectFour(models.Model):
    room_name = models.CharField(max_length=254, default="None")
    current_player = models.IntegerField(default=1)

    def __str__(self):
        return self.room_name