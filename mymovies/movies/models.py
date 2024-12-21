from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(
        null=True, unique=True
    )  # Permitimos nulos temporalmente
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    overview = models.TextField()
    release_date = models.DateField()
    poster_url = models.URLField()
    vote_average = models.FloatField()

    def __str__(self):
        return self.title
