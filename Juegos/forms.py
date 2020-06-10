from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class PlayerCreationForm(UserCreationForm):
    class Meta:
        fields = ('username',)
        model = get_user_model()
    
    def __init__(self, *args, **kwargs):
       super(UserCreationForm, self).__init__(*args, **kwargs)
       # no authentication needed
       self.fields['password1'].required = False
       self.fields['password2'].required = False
       self.fields['password1'].widget.attrs['autocomplete'] = 'off'
       self.fields['password2'].widget.attrs['autocomplete'] = 'off'
       self.fields['password1'].widget = forms.HiddenInput()
       self.fields['password2'].widget = forms.HiddenInput()


class JuegoCreationForm(forms.ModelForm):
    CHOICES = [(0, 'Player 1'), (1, 'Player 2')]
    serving = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    error_messages = {
        'same_player' : "Un jugador no puede jugar con si mismo",
    }

    def clean_player2(self):
        player1 = self.cleaned_data.get("player1")
        player2 = self.cleaned_data.get("player2")
        if player1.id == player2.id:
            raise forms.ValidationError(
                self.error_messages['same_player'],
                code='same_player'
            )
        return player2

    class Meta:
        model = Juego
        fields = ("player1", "player2", "serving")


