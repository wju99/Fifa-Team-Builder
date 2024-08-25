from django.db import models

class TacticalStyle(models.TextChoices):
    TIKI_TAKA = 'TT', 'Tiki Taka'
    GEGENPRESS = 'GP', 'Gegenpress'
    PARK_THE_BUS = 'PTB', 'Park the Bus'
    COUNTER_ATTACK = 'CA', 'Counter Attack'
    KICK_AND_RUSH = 'KR', 'Kick and Rush'
    WINGPLAY = 'WP', 'Wingplay'

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    overall_rating = models.IntegerField()
    tactical_style = models.CharField(
        max_length=3,
        choices=TacticalStyle.choices,
        default=TacticalStyle.TIKI_TAKA
    )

    def __str__(self):
        return f"{self.name} - {self.position} ({self.get_tactical_style_display()})"