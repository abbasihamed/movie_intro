# Generated by Django 3.1.6 on 2021-03-15 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20210315_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='movie_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rec', to='movies.movielist'),
        ),
    ]
