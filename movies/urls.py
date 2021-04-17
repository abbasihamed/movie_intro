from django.urls import path
from movies.views import Movies, ActorMovie, GenreMovie, RecList

urlpatterns = [
    path('movie/list/', Movies.as_view()),
    path('actor-movie/list/<str:actor>/', ActorMovie.as_view()),
    path('genre-movie/list/<str:genre>/', GenreMovie.as_view()),
    path('recommended/list/', RecList.as_view()),
]
