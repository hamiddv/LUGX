# Generated by Django 4.2.7 on 2023-12-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_rename_summary_contact_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
    ]
