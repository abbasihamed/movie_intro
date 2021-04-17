from django.db import models
from movie_genre.models import Genre


class MovieList(models.Model):
    name = models.CharField(max_length=250, unique=False)
    Actor = models.ManyToManyField('Actor', through='Movie_Actor', related_name='actor_movie')
    rate = models.FloatField()
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    image = models.ImageField(upload_to='image/movies/')
    description = models.TextField()
    release_date = models.DateField()
    trailer_link = models.URLField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='image/actors/')
    age = models.DateField()
    movie = models.ManyToManyField(MovieList, through='Movie_Actor')

    def __str__(self):
        return self.name


class Rec(models.Model):
    movie_name = models.OneToOneField(MovieList, on_delete=models.CASCADE, unique=True, related_name='movie_rec')

    def save(self, *args, **kwargs):
        if Rec.objects.all().count() >= 3:
            print(Rec.objects.all().count())
            return
        else:
            super().save(*args, *kwargs)

    def __str__(self):
        return self.movie_name.name


class Movie_Actor(models.Model):
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE, related_name='movie')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='actor')

    def __str__(self):
        return f'{self.movie} || {self.actor}'

    class Meta:
        unique_together = [['movie', 'actor']]
