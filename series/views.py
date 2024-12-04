from django.shortcuts import render,get_object_or_404
from .models import Serie

def all_series(request):
    series = Serie.objects.all() 
    return render(request, 'series/all_series.html', {'series': series})

def detail(request,serie_id):
    series = get_object_or_404(Serie, pk=serie_id)
    return render(request, 'series/detail.html', {'series':series})

def home(request):
    series = Serie.objects.all()
    return render(request, 'mproject/home.html', {'series':series})
