from django.shortcuts import render,get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def detail(request,movie_id):
    movies = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movies': movies})

def home(request):
    movies = Movie.objects.all()
    return render(request, 'mproject/home.html', {'movies':movies})
