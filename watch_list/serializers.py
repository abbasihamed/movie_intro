from rest_framework import serializers

from movies.serializers import MovieListSerializers
from watch_list.models import WatchList


class WatchListSerializers(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    movie = MovieListSerializers(read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'
