from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ConnectFour
from .serializers import ConnectFourSerializer

def index(request):
    return render(request, 'frontend/index.html')

@api_view(['POST'])
def make_move(request, game_id):
    game = ConnectFour.objects.get(pk=game_id)
    column = request.data.get('column')

    if column < 0 or column > 6:
        return Response({"error": "Invalid column"}, status=status.HTTP_400_BAD_REQUEST)

    board = [list(game.board[i:i+7]) for i in range(0, 42, 7)]

    for row in reversed(board):
        if row[column] == '.':
            row[column] = 'X' if game.current_player == 1 else 'O'
            game.current_player = 2 if game.current_player == 1 else 1
            break
    else:
        return Response({"error": "Column is full"}, status=status.HTTP_400_BAD_REQUEST)

    game.board = ''.join([''.join(row) for row in board])
    game.save()
    
    return Response(ConnectFourSerializer(game).data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_board(request, game_id):
    game, created = ConnectFour.objects.get_or_create(pk=game_id)
    return Response(ConnectFourSerializer(game).data, status=status.HTTP_200_OK)