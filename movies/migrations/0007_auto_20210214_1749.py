# Generated by Django 3.1.6 on 2021-02-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20210214_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='image',
            field=models.ImageField(upload_to='image/actors'),
        ),
        migrations.AlterField(
            model_name='movielist',
            name='image',
            field=models.ImageField(upload_to='image/movies/'),
        ),
    ]