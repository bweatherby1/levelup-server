# Generated by Django 4.1.3 on 2024-05-21 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_alter_game_game_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='levelupapi.gamer'),
        ),
    ]
