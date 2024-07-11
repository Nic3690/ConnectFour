from django.urls import path
from . import views

urlpatterns = [
    path('make_move/<int:game_id>/', views.make_move, name='make_move'),
    path('get_board/<int:game_id>/', views.get_board, name='get_board'),
]