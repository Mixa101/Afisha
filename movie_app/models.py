from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255, verbose_name="Режиссер")
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    duration = models.TimeField(verbose_name="Длительность")
    director = models.ForeignKey(Director ,on_delete=models.CASCADE, related_name="director")    
    
    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=255, verbose_name="Отзыв")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie")    
    
    def __str__(self):
        return self.text
