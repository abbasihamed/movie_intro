from rest_framework import serializers
from user_profile.models import Profile, UserRegister


# class UserRegisterSerializer(serializers.ModelSerializer):
#     profile = serializers.StringRelatedField(read_only=True, many=True)
#
#     class Meta:
#         model = UserRegister
#         fields = ['id', 'email', 'username', 'profile']


class ProfileSerializers(serializers.ModelSerializer):
    # user = UserRegisterSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    # profile = serializers.StringRelatedField(read_only=True, many=True)
    profile = ProfileSerializers(read_only=True)

    class Meta:
        model = UserRegister
        fields = ['id', 'email', 'username', 'profile']
