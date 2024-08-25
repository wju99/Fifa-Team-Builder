from django.contrib import admin

# Register your models here.
from .models import TacticalStyle, Player

admin.site.register(TacticalStyle)
admin.site.register(Player)