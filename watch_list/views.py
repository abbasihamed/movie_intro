from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from watch_list.models import WatchList
from watch_list.serializers import WatchListSerializers
from movies.models import MovieList


# Create your views here.

class UserWatchList(APIView):
    def get(self, request):
        try:
            user = request.user
            query = WatchList.objects.filter(owner=user)
            serializer = WatchListSerializers(query, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'Server not available'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        user = request.user
        serializer = WatchListSerializers(data=request.data, context={'request': request})
        movie = request.data['movie']
        items = MovieList.objects.get(name=movie)
        watchlist = WatchList.objects.filter(movie__name=items, owner=user)
        if not watchlist:
            if serializer.is_valid():
                serializer.save(owner=user, movie=items)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)
        else:
            return Response({'status': 'Already exist'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query = WatchList.objects.get(pk=pk, owner=request.user)
        query.delete()
        return Response({'status': 'Item deleted'}, status=status.HTTP_200_OK)
