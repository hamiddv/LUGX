# Generated by Django 4.2 on 2023-12-01 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/categories/%y/%m/%d/', verbose_name='image')),
                ('caption', models.TextField(blank=True, max_length=1024, null=True, verbose_name='caption')),
                ('is_top', models.BooleanField(default=True, verbose_name='is top')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('caption', models.TextField(max_length=1024, verbose_name='caption')),
                ('descriptions', models.TextField(max_length=5024, verbose_name='descriptions')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('discount_percent', models.PositiveIntegerField(blank=True, null=True, verbose_name='discount percent')),
                ('most_played_image', models.ImageField(help_text='this is for dont resizing the image in site if this game is most played', upload_to='media/games/most_played_image/%y/%m/%d/', verbose_name='most played image')),
                ('most_discounted_image', models.ImageField(help_text='this is for dont resizing the image in site if this game is most discounted', upload_to='media/games/most_discount_image/%y/%m/%d/', verbose_name='most discounted image')),
                ('image', models.ImageField(upload_to='media/games/image/%y/%m/%d/')),
                ('game_id', models.CharField(max_length=10, verbose_name='game id')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('most_played', models.BooleanField(default=True, verbose_name='most played')),
                ('is_trending', models.BooleanField(default=True, verbose_name='is trending')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='created date')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'game',
                'verbose_name_plural': 'game',
            },
        ),
        migrations.CreateModel(
            name='Gener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='created date')),
            ],
            options={
                'verbose_name': 'gener',
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='GameGener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('gener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.gener')),
            ],
            options={
                'unique_together': {('game', 'gener')},
            },
        ),
        migrations.AddConstraint(
            model_name='game',
            constraint=models.UniqueConstraint(fields=('most_played', 'is_trending'), name='unique_fields'),
        ),
    ]