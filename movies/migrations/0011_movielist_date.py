# Generated by Django 3.1.6 on 2021-03-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20210214_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
