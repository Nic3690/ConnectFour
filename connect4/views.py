from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ConnectFour
from .serializers import ConnectFourSerializer

def index(request):
    return render(request, 'frontend/index.html')

def check_winner(board, x, y, player):
    def count_consecutive(dx, dy):
        count = 0
        for i in range(1, 4):
            nx, ny = x + i*dx, y + i*dy
            if 0 <= nx < 7 and 0 <= ny < 6 and board[ny][nx] == player:
                count += 1
            else:
                break
        return count

    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        total_count = 1 + count_consecutive(dx, dy) + count_consecutive(-dx, -dy)
        if total_count >= 4:
            return True
    return False

@api_view(['POST'])
def make_move(request, game_id):
    game = ConnectFour.objects.get(pk=game_id)
    column = request.data.get('column')

    if column < 0 or column > 6:
        return Response({"error": "Invalid column"}, status=status.HTTP_400_BAD_REQUEST)

    board = [list(game.board[i:i+7]) for i in range(0, 42, 7)]
    row_index = None
    player = 'X' if game.current_player == 1 else 'O'

    for row in reversed(board):
        if row[column] == '.':
            row[column] = player
            row_index = board.index(row)
            game.current_player = 2 if game.current_player == 1 else 1
            break
    else:
        return Response({"error": "Column is full"}, status=status.HTTP_400_BAD_REQUEST)

    game.board = ''.join([''.join(row) for row in board])
    game.save()

    is_winner = check_winner(board, column, row_index, player)
    winner = game.current_player if is_winner else None
    
    return Response({"board": game.board, "winner": winner}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_board(request, game_id):
    game, created = ConnectFour.objects.get_or_create(pk=game_id)
    board = [list(game.board[i:i+7]) for i in range(0, 42, 7)]

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell != '.' and check_winner(board, y, x, cell):
                return Response({"board": game.board, "winner": 'X' if game.current_player == 2 else 'O'}, status=status.HTTP_200_OK)

    return Response(ConnectFourSerializer(game).data, status=status.HTTP_200_OK)

@api_view(['POST'])
def reset_game(request, game_id):
    game = ConnectFour.objects.get(pk=game_id)
    game.board = '.' * 42
    game.current_player = 1
    game.save()
    return Response(ConnectFourSerializer(game).data, status=status.HTTP_200_OK)