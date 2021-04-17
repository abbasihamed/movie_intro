from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies.models import MovieList, Actor, Rec
from movies.serializers import MovieListSerializers, ActorSerializers, RecSerializers


# Create your views here.
# تابع گرفتن تموم فیلم های موجود در دیتابیس
class Movies(APIView):
    def get(self, request):
        query = MovieList.objects.all().order_by('-date')
        serializers = MovieListSerializers(query, many=True, context={'request': request})
        if serializers.data != '':
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'statue': 'Not find data'}, status=status.HTTP_404_NOT_FOUND)


# تابع گرفتن فیلم های ژانر خاص
class GenreMovie(APIView):
    def get(self, request, genre):
        # کوئری گرفتن ژانر ارسال شده
        query = MovieList.objects.filter(genre__genre__icontains=genre)
        serializers = MovieListSerializers(query, many=True, context={'request':request})
        if serializers.data != '':
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'statue': 'Not find data'}, status=status.HTTP_404_NOT_FOUND)


# تابع گرفتن فیلم های بازیگر خاص
class ActorMovie(APIView):
    def get(self, request, actor):
        query = Actor.objects.filter(name__icontains=actor)
        serializers = ActorSerializers(query, many=True, context={'request': request})
        if serializers.data != '':
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'statue': 'Not find data'}, status=status.HTTP_404_NOT_FOUND)


class RecList(APIView):
    def get(self, request):
        query = Rec.objects.all()
        serializers = RecSerializers(query, many=True, context={'request': request})
        if serializers.data != '':
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'No items'}, status=status.HTTP_404_NOT_FOUND)
