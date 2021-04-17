from django.urls import path
from user_profile.views import UserProfile, UserRegisterList

urlpatterns = [
    path('user/register/<int:pk>', UserRegisterList.as_view()),
    path('user/profile/', UserProfile.as_view()),
    path('user/register/', UserRegisterList.as_view()),
]
