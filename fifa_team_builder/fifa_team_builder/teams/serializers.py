from rest_framework import serializers
from .models import Player, TacticalStyle

class PlayerSerializer(serializers.ModelSerializer):
    tactical_style = serializers.ChoiceField(choices=TacticalStyle.choices)

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'overall_rating', 'tactical_style']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tactical_style'] = instance.get_tactical_style_display()
        return representation