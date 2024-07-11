from django.db import models

class ConnectFour(models.Model):
    board = models.CharField(max_length=42, default="." * 42)
    current_player = models.IntegerField(default=1)

    def __str__(self):
        return self.board