# Generated by Django 4.2 on 2023-12-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_gamegener_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='game',
            name='unique_fields',
        ),
        migrations.AlterField(
            model_name='game',
            name='is_trending',
            field=models.BooleanField(verbose_name='is trending'),
        ),
        migrations.AlterField(
            model_name='game',
            name='most_played',
            field=models.BooleanField(verbose_name='most played'),
        ),
        migrations.AlterUniqueTogether(
            name='gamegener',
            unique_together={('game', 'gener')},
        ),
        migrations.AlterUniqueTogether(
            name='gametag',
            unique_together={('game', 'tag')},
        ),
    ]
