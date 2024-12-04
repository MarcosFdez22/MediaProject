from django.shortcuts import render
from series.models import Serie  
from movies.models import Movie
def home(request):
    movies = Movie.objects.all()  
    series = Serie.objects.all()  
    return render(request, 'mproject/home.html', {'movies': movies, 'series': series})
