from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Count

from .models import *
from .forms import *


def addP1(request, *args, **kwargs):
    game = Juego.objects.get(id=kwargs['pk'])
    game.score1 += 1
    if (game.score1 - game.score2)**2 >= 4 and (game.score1 > 10 or game.score2 > 10):
        game.finished = 1
        game.winner = 0
    game.save()
    return redirect('game_details', kwargs['pk'])

def addP2(request, *args, **kwargs):
    game = Juego.objects.get(id=kwargs['pk'])
    game.score2 += 1
    if (game.score1 - game.score2)**2 >= 4 and (game.score1 > 10 or game.score2 > 10):
        game.finished = 1
        game.winner = 1
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

    def get_initial(self, *args, **kwargs):
        initial = super(GameCreationView, self).get_initial()
        initial = initial.copy()
        # shouldn't be done like this, but I am short on time, should have a placeholder user
        initial['winner'] = User.objects.get(id = 1)
        return initial

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
        lista_jugadores = get_user_model().objects.filter(is_active = True)
        juegos = Juego.objects.filter(finished=1).values()
        jugadores = dict()
        for i in juegos:
            winner = get_user_model().objects.get(pk=[i['player1_id'], i['player2_id']][i['winner']]).username
            if winner not in jugadores:
                jugadores[winner] = 0
            jugadores[winner] += 1
        print(jugadores)
        return jugadores