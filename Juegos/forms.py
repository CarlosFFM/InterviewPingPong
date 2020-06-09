from django import forms
from .models import *

class JuegoCreationForm(forms.ModelForm):
    CHOICES = [(0, 'Player 1'), (1, 'Player 2')]
    serving = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = Juego
        fields = ("player1", "player2", "serving")
