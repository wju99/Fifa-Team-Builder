# Generated by Django 4.2.15 on 2024-08-25 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_remove_tacticalstyle_description_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TacticalStyle',
        ),
        migrations.AddField(
            model_name='player',
            name='tactical_style',
            field=models.CharField(choices=[('TT', 'Tiki Taka'), ('GP', 'Gegenpress'), ('PTB', 'Park the Bus'), ('CA', 'Counter Attack'), ('KR', 'Kick and Rush'), ('WP', 'Wingplay')], default='TT', max_length=3),
        ),
    ]
