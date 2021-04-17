from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from user_profile.models import UserRegister, Profile
from user_profile.serializers import ProfileSerializers, UserRegisterSerializer


# Create your views here.

class UserProfile(APIView):

    def get(self, request):
        try:
            user = request.user
            query = Profile.objects.get(user=user)
            serializers = ProfileSerializers(query, context={'request': request})
            if serializers.data != '':
                return Response(serializers.data, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'user not find'}, status=status.HTTP_404_NOT_FOUND)
        except:
            print(request.user)
            return Response({'status': 'User Profile not exist'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user = request.user
        query = Profile.objects.filter(user=user)
        serializers = ProfileSerializers(query, data=request.data)
        if not query:
            serializers.save(user=user)
            return Response({'status': 'not find'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': 'Already exist'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = request.user
        email = request.data['email']
        username = request.data['username']
        query = Profile.objects.get(pk=pk)
        serializers = ProfileSerializers(query, data=request.data)
        userinfo = UserRegister.objects.filter(username=user)
        print(userinfo)
        if serializers.is_valid():
            serializers.save(user=user, user_username=username, user_email=email)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterList(APIView):
    def get(self, request):
        query = UserRegister.objects.get(username=request.user)
        serializers = UserRegisterSerializer(query, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = UserRegister.objects.get(pk=pk)

        serializer = UserRegisterSerializer(query, data=request.data)
        if serializer.is_valid():
            user = UserRegister()
            user.id = serializer.data.get('id')
            user.username = serializer.data.get('username')
            user.email = serializer.data.get('email')
            # user.data_join =
            user.profile.show_name = serializer.data.get('profile')['show_name']

            user.profile.bio = serializer.data.get('profile')['bio']
            user.profile.image = request.FILES['image']
            user.save()

            # user.profile.show_name
            # email = serializer.data.get('email')
            # email = serializer.data.get('email')
            # print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
