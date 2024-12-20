from django.urls import path
from .views import (MoviesReviewsList,
                    MoviesList, DirectorsList, ReviewsList, MovieDetail,
                    ReviewDetail, DirectorDetail)

urlpatterns = [
    path('movies/', MoviesList.as_view()),
    path('movies/reviews/', MoviesReviewsList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('reviews/', ReviewsList.as_view()),
    path('reviews/<int:pk>', ReviewDetail.as_view()),
    path('directors/<int:pk>', DirectorDetail.as_view()),
    path('directors/', DirectorsList.as_view()),
]