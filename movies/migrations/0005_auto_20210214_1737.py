# Generated by Django 3.1.6 on 2021-02-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20210214_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='rate',
            field=models.FloatField(),
        ),
    ]
