# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from movie_genre.models import Genre
# from movie_genre.serializers import GenreSerializers
#
#
# # Create your views here.
# class GenreMovie(APIView):
#     def get(self, request):
#         query = Genre.objects.all()
#         serializers = GenreSerializers(query, many=True)
#         if serializers.data != '':
#             return Response(serializers.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'statue': 'Not find data'}, status=status.HTTP_404_NOT_FOUND)
