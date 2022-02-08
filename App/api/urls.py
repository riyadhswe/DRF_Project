from django.urls import path
from App.api.views import movie_list,movie_details
urlpatterns = [
    path('',movie_list,name='movie_list'),
    path('<int:pk>',movie_details,name='movie_details'),
]