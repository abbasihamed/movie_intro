from django.db import models
from movies.models import MovieList
from user_profile.models import UserRegister


class WatchList(models.Model):
    owner = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieList, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.username
