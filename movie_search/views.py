from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from movies.models import MovieList, Actor
from movies.serializers import MovieListSerializers, ActorSerializers


# Create your views here.

# کلاس جستجوی فیلم با استفاده از عنوان
class SearchMovie(APIView):
    def get(self, request):
        params = request.GET['t']  # گرفتن عنوان جنسجو شده با کلید t

        query = MovieList.objects.filter(name__contains=params)  # جستجوی عنوان ارسال شده

        serializers = MovieListSerializers(query, many=True, context={'request': request})
        if not query:
            return Response({'status': 'not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(serializers.data, status=status.HTTP_200_OK)
