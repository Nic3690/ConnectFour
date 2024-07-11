from rest_framework import serializers
from .models import ConnectFour

class ConnectFourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectFour
        fields = ['id', 'board', 'current_player']