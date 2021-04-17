from rest_framework import serializers
from movies.models import MovieList, Actor, Movie_Actor, Rec


class MovieActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie_Actor
        fields = '__all__'


class MovieListSerializers(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(read_only=True, many=True)
    Actor = serializers.StringRelatedField(many=True)

    class Meta:
        model = MovieList
        fields = '__all__'


class ActorSerializers(serializers.ModelSerializer):
    movie = MovieListSerializers(many=True)

    class Meta:
        model = Actor
        fields = '__all__'


class RecSerializers(serializers.ModelSerializer):
    movie_name = MovieListSerializers(read_only=True)

    class Meta:
        model = Rec
        fields = ['movie_name']
