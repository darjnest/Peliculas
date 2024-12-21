import requests
from .models import Movie


def fetch_movies():
    for page in range(1, 6):  # Obtener las primeras 5 páginas
        url = f"https://api.themoviedb.org/3/movie/popular?api_key=917c1c408e08bb7f5ba23552d76b3746&page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            for movie_data in data["results"]:
                if not Movie.objects.filter(movie_id=movie_data["id"]).exists():
                    poster_url = (
                        f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
                    )
                    movie = Movie(
                        movie_id=movie_data["id"],
                        title=movie_data["title"],
                        original_title=movie_data["original_title"],
                        overview=movie_data["overview"],
                        release_date=movie_data["release_date"],
                        poster_url=poster_url,
                        vote_average=movie_data["vote_average"],
                    )
                    movie.save()
        else:
            print("Error al obtener los datos de la API")
