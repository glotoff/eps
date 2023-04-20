import uuid
from django.db import models
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from ..common.models import BaseEntity
from ..clubs.models import Club
from ..tournaments.models import Tournament

# Create your models here.
"""
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

auditlog.register(Player)
"""


class Player(BaseEntity):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=False)
    clubs = models.ManyToManyField(Club, through="PlayerClub")
    tournaments = models.ManyToManyField(Tournament, through="PlayerTournament")


class PlayerClub(BaseEntity):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    class Meta:
        db_table = 'player_club_relation'


class PlayerTournament(BaseEntity):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournaments = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    class Meta:
        db_table = 'player_tournament_relation'


auditlog.register(Player)
auditlog.register(PlayerClub)
auditlog.register(PlayerTournament)
