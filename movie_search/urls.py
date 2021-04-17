from django.urls import path
from movie_search.views import SearchMovie

urlpatterns = [
    path('search/', SearchMovie.as_view()),
]
