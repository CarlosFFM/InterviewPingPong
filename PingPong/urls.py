
from django.contrib import admin
from django.urls import path
from Juegos.views import *

urlpatterns = [
    path('', ListaJuegos.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('add_player/', PlayerCreationView.as_view(), name="add_player"),
    path('games/', ListaJuegos.as_view(), name="Juegos"),
    path('games/details/<int:pk>/', GamesDetailView.as_view(), name='game_details'),
    #can be done with another parameter, but it is faster to develop it like this
    path('games/edit/addP/<int:pk>/<int:pl>', addP, name='addP'),
    path('create_game/', GameCreationView.as_view(), name="new_game"),
    path('leaderboard/', Leaderboard.as_view(), name="leaderboard"),
]
