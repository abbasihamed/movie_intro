from django.contrib import admin
from movies.models import MovieList, Actor, Movie_Actor, Rec

# Register your models here.
admin.site.register(MovieList)
admin.site.register(Actor)
admin.site.register(Movie_Actor)
admin.site.register(Rec)
