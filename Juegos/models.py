from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import redirect, reverse

class Juego(models.Model):
    player1 = models.ForeignKey(User, models.DO_NOTHING, related_name="player1", db_column='player1')
    player2 = models.ForeignKey(User, models.DO_NOTHING, related_name="player2", db_column='player2')
    score1 = models.IntegerField(blank=True, null=True, default=0)
    score2 = models.IntegerField(blank=True, null=True, default=0)
    turn = models.IntegerField(blank=True, null=True, default=1)
    serving = models.IntegerField()
    finished = models.IntegerField(default=0)
    fecha = models.DateField(null=False, blank=True, default=now)
    winner = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('game_details', kwargs={'pk': self.pk})

    def __str__(self):
            return "{} vs. {} Score: {} - {}".format(self.player1, self.player2, self.score1, self.score2)

    def save(self, *args, **kwargs):
        if self.player1 != self.player2:
            super().save()
        else:
            print("No se guarda")

    class Meta:
        managed = True
        db_table = 'Juego'
        verbose_name= 'Juego'
