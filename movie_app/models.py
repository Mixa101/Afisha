from django.db import models

STARS = [
    (i, "*" * i) for i in range(1, 5)
]

class Director(models.Model):
    name = models.CharField(max_length=255, verbose_name="Режиссер")
    
    def __str__(self):
        return self.name
    
    # MOVIE COUNTER 
    @property
    def movies_count(self):
        return len(self.movie.all())
    
    # FOR OUTPUT 
    @property
    def movies_names(self):
        movies = self.movie.all()
        return [movie.title for movie in movies]

class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    duration = models.DurationField()
    director = models.ForeignKey(Director ,on_delete=models.CASCADE, related_name="movie")
    
    def __str__(self):
        return self.title
    @property
    def director_(self):
        return self.director.name
    
    # FOR REVIEWS LIST
    @property
    def reviews_(self):
        reviews = self.reviews.all()
        return [review.review_text_and_stars for review in reviews]
    
    # FOR GET AVERAGE RATE
    @property
    def average_rate(self):
        rates = self.reviews.all()
        if rates:
            return sum([rate.stars for rate in rates]) / rates.count()
        return "There is no reviews"


class Review(models.Model):
    text = models.CharField(max_length=255, verbose_name="Отзыв")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField(choices=STARS, default=5)
    def __str__(self):
        return self.text
    
    # FOR LOOKING GOOD OUTPUT XD
    @property
    def review_text_and_stars(self):
        return f"{self.text}; оценка : {self.stars}"

