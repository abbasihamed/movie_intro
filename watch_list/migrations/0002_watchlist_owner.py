# Generated by Django 3.1.6 on 2021-02-17 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('watch_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_profile.userregister'),
            preserve_default=False,
        ),
    ]
