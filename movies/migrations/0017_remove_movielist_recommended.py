# Generated by Django 3.1.6 on 2021-03-16 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0016_remove_rec_recommended'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielist',
            name='recommended',
        ),
    ]
