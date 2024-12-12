from django.urls import path
from .views import (MoviesReviewsList,
                    MoviesList, DirectorsList, ReviewsList, MovieDetail,
                    ReviewDetail, DirectorDetail)

urlpatterns = [
    path('api/v1/movies/', MoviesList.as_view()),
    path('api/v1/movies/reviews/', MoviesReviewsList.as_view()),
    path('api/v1/movies/<int:pk>', MovieDetail.as_view()),
    path('api/v1/reviews/', ReviewsList.as_view()),
    path('api/v1/reviews/<int:pk>', ReviewDetail.as_view()),
    path('api/v1/directors/<int:pk>', DirectorDetail.as_view()),
    path('api/v1/directors/', DirectorsList.as_view()),
]