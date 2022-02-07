from django.shortcuts import render
from .models import *
from django.http import JsonResponse


# Create your views here.
def movie_list(request):
    movie = Movie.objects.all()
    list(movie.values())

    return JsonResponse()
