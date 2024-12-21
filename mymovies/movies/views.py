from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Movie
from .services import fetch_movies


def home(request):
    fetch_movies()
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 10)  # Muestra 10 películas por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "movies/home.html", {"page_obj": page_obj})
