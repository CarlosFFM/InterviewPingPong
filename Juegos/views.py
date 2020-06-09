from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User

from .models import *
from .forms import *

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