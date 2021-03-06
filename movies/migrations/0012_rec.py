# Generated by Django 3.1.6 on 2021-03-14 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_movielist_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommended', models.BooleanField(default=False)),
                ('movie_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rec', to='movies.movielist')),
            ],
        ),
    ]
