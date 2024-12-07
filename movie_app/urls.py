from django.urls import path
from .views import (movies_list_api_view, reviews_list_api_view,
                    movies_detail_list_view, reviews_detail_list_view, directors_detail_view,
                    movies_reviews_detail_view, movies_reviews_list_view, directors_list_view)

urlpatterns = [
    path('api/v1/reviews/', reviews_list_api_view),
    path('api/v1/movies/', movies_list_api_view),
    path('api/v1/movies/reviews/', movies_reviews_list_view),
    path('api/v1/movies/reviews/<int:id>', movies_reviews_detail_view),
    path('api/v1/movies/<int:id>', movies_detail_list_view),
    path('api/v1/reviews/<int:id>', reviews_detail_list_view),
    path('api/v1/directors/<int:id>', directors_detail_view),
    path('api/v1/directors/', directors_list_view),
]