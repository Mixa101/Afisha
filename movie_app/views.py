from .models import Movie, Review, Director
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *


# views for get all models objects in one JSON
@api_view(['GET'])
def movies_list_api_view(request):
    # step 1
    movies = Movie.objects.all()
    
    # step 2
    serializer = MovieSerializer(instance = movies, many = True)
    
    # step 3
    return Response(data=serializer.data)

@api_view(['GET'])
def reviews_list_api_view(request):
    # step 1
    reviews = Review.objects.all()
    
    # step 2
    serializer = ReviewSerializer(instance = reviews, many = True)
    
    # step 3
    return Response(data=serializer.data)

@api_view(['GET'])
def directors_list_api_view(request):
    # step 1
    directors = Director.objects.all()
    
    # step 2
    serializer = DirectorSerializer(instance = directors, many = True)
    
    # step 3
    return Response(data=serializer.data)

# views for detailed models
@api_view(['GET'])
def movies_detail_list_view(request, id):
    # step 1
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={"ERROR!": 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # step 2
    data = MovieDetailSerializer(movie).data
    
    # step 3
    return Response(data=data)

@api_view(['GET'])
def reviews_detail_list_view(request, id):
    # step 1
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={"ERROR!": 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # step 2
    data = ReviewDetailSerializer(review).data
    
    # step 3
    return Response(data=data)


@api_view(['GET'])
def directors_detail_list_view(request, id):
    # step 1
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={"ERROR!": 'movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # step 2
    data = DirectorDetailSerializer(director).data
    
    # step 3
    return Response(data=data)