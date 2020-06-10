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

    class Meta:
        model = Juego
        fields = ("player1", "player2", "serving")


