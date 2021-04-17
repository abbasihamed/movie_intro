from django.db import models


# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=300)

    def __str__(self):
        return self.genre
