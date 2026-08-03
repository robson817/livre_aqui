from django.shortcuts import get_object_or_404, render

from .forms import MovieSearchForm
from .models import Movie

# Create your views here.

def movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie.html', {'movie': movie})

def movie_search(request):
    form = MovieSearchForm(request.GET)
    movies = Movie.objects.all()
    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            movies = movies.filter(title__icontains=query)
    return render(request, 'movie_search.html', {'form': form, 'movies': movies})