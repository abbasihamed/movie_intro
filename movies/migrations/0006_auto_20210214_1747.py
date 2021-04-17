# Generated by Django 3.1.6 on 2021-02-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_genre', '0001_initial'),
        ('movies', '0005_auto_20210214_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='genre',
        ),
        migrations.AddField(
            model_name='movielist',
            name='genre',
            field=models.ManyToManyField(to='movie_genre.Genre'),
        ),
    ]