# Generated by Django 4.2 on 2023-12-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('logo', models.ImageField(upload_to='media/features/%y/%m/%d', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
            },
        ),
    ]
