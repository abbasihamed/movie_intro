from django.urls import path
from watch_list.views import UserWatchList

urlpatterns = [
    path('watch/list/', UserWatchList.as_view()),
    path('watch/list/<int:pk>', UserWatchList.as_view()),
]
