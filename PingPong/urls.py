
from django.contrib import admin
from django.urls import path
from Juegos.views import *

urlpatterns = [
    path('', ListaJuegos.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('games/', ListaJuegos.as_view(), name="Juegos"),
    path('games/details/<int:pk>/', GamesDetailView.as_view(), name='game_details'),
    path('create_game/', GameCreationView.as_view(), name="new_game"),
    path('leaderboard/', ListaJuegos.as_view(), name="leaderboard"),
]
