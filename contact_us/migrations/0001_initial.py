# Generated by Django 4.2.7 on 2023-12-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('summary', models.CharField(max_length=128, verbose_name='summary')),
                ('subject', models.CharField(max_length=128, verbose_name='subject')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'contact us message',
                'verbose_name_plural': 'contact us messages',
            },
        ),
    ]
