from django.urls import path
from App.api.views import StreamPlatformAV,WatchlistAV
urlpatterns = [
    path('',WatchlistAV.as_view(),name='strem'),
    path('s',StreamPlatformAV.as_view(),name='movie_details'),
]
