# Generated by Django 4.2 on 2023-12-01 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_detail_image_alter_game_most_discounted_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='created date')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now=True, verbose_name='created date'),
        ),
        migrations.AddField(
            model_name='gamegener',
            name='created_date',
            field=models.DateTimeField(auto_now=True, verbose_name='created date'),
        ),
        migrations.CreateModel(
            name='GameTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='created date')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.tag')),
            ],
            options={
                'unique_together': {('game', 'tag')},
            },
        ),
    ]
