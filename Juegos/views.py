from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.contrib import messages

from .models import *
from .forms import *


def add_p(request, *args, **kwargs):
    game = Juego.objects.get(id=kwargs['pk'])
    game.turn += 1
    if game.turn % 2 > 0:
        game.serving = int(not bool(game.serving))
    if kwargs['pl']:
        game.score2 += 1
    else:
        game.score1 += 1
    if (game.score1 - game.score2)**2 >= 4 and (game.score1 > 10 or game.score2 > 10):
        game.finished = 1
        if kwargs['pl']:
            game.winner = 1
        else:
            game.winner = 0
        messages.success(request, "Gana {}".format([game.player1, game.player2][game.winner]))
    game.save()
    return redirect('game_details', kwargs['pk'])

class ListaJuegos(ListView):
    model = Juego
    template_name = 'Juego/juegos_listView.html'
    context_object_name = "juegos"
    ordering = ['-fecha']

    # leave it like that in case further changes are necessary
    def get_queryset(self):
        juegos = Juego.objects.filter(finished=False)
        return juegos

class GamesDetailView(DetailView):
    model = Juego
    template_name = 'Juego/juegos_detailView.html'
    

class GameCreationView(CreateView):
    model = Juego
    template_name = 'Juego/juegos_createView.html'
    form_class = JuegoCreationForm

class PlayerCreationView(CreateView):
    model = get_user_model()
    template_name = 'Juego/player_createView.html'
    form_class = PlayerCreationForm
    success_url = '/'

class Leaderboard(ListView):
    model = get_user_model()
    template_name = 'Juego/player_listView.html'
    context_object_name = "jugadores"

    # leave it like that in case further changes are necessary
    def get_queryset(self):
        juegos = Juego.objects.filter(finished=1).values()
        jugadores = dict()
        for i in juegos:
            winner = get_user_model().objects.get(pk=[i['player1_id'], i['player2_id']][i['winner']]).username
            if winner not in jugadores:
                jugadores[winner] = 0
            jugadores[winner] += 1
        print(jugadores)
        return jugadores