# Generated by Django 3.1.6 on 2021-03-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_auto_20210315_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rec',
            name='recommended',
            field=models.BooleanField(),
        ),
    ]
