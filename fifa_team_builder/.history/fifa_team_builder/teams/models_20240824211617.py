from django.db import models

# Create your models here.

class TacticalStyle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    overall_rating = models.IntegerField()
    # Add more fields as needed (e.g., pace, shooting, passing, etc.)

    def __str__(self):
        return f"{self.name} - {self.position}"