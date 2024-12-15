from .models import Movie, Review, Director
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *


# views for get all models objects in one JSON

# THIS FOR LIST OF MOVIES
class MoviesList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(instance = movies, many = True).data
        return Response(serializer)
    
    def post(self, request):
        new_movie = MovieDetailSerializer(data=request.data)
        if new_movie.is_valid():
            new_movie.save()
            return Response(new_movie.data, status=status.HTTP_201_CREATED)
        return Response(new_movie.errors, status=status.HTTP_400_BAD_REQUEST)


# THIS FOR LIST OF REVIEWS
class ReviewsList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(instance = reviews, many = True).data
        return Response(serializer)
    
    def post(self, request):
        # Легче все сделать через сериализатор
        new_review = ReviewValidateSerializer(data=request.data)
        
        if new_review.is_valid():
            new_review.save()
            return Response(data={"succesfuly create Review: good"}, status=status.HTTP_201_CREATED)
        return Response(new_review.errors, status=status.HTTP_400_BAD_REQUEST)
        

# THIS FOR LIST OF DIRECTORS
class DirectorsList(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(instance = directors, many = True).data
        return Response(serializer)
    
    def post(self, request):
        new_director = DirectorValidateSerializer(data=request.data)
        
        if new_director.is_valid():
            new_director.save()
            return Response(data={"succesfuly create director": f"{new_director.data['name']}"}, status=status.HTTP_201_CREATED)
        return Response(new_director.errors, status=status.HTTP_400_BAD_REQUEST)


# THIS FOR DETAIL OF MOVIE
class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return {"Error!": "movie not found"}
    
    def get(self, request, pk):
        movie = self.get_object(pk)
        if isinstance(movie, Movie):
            serializer = MovieDetailSerializer(instance = movie).data
            return Response(serializer)
        else:
            return Response(data=movie, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieDetailSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# THIS FOR DETAIL OF REVIEW
class ReviewDetail(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return {"Error!": "review not found"}
    
    def get(self, request, pk):
        review = self.get_object(pk)
        if isinstance(review, Review):
            serializer = ReviewDetailSerializer(instance=review).data
            return Response(data=serializer)
        else:
            return Response(data=review, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# THIS FOR DETAIL OF DIRECTOR
class DirectorDetail(APIView):
    def get_object(self, pk):
        try:
            return Director.objects.get(pk=pk)
        except Director.DoesNotExist:
            return {"Error!": "director not found"}
    
    def get(self, request, pk):
        director = self.get_object(pk)
        if isinstance(director, Director):
            serializer = DirectorDetailSerializer(instance=director).data
            return Response(data=serializer)
        else:
            return Response(data=director, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorValidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        director = self.get_object(pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            

# THIS FOR MOVIES WITH THEIR REVIEWS
class MoviesReviewsList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MoviesReviewsSerializer(movies, many=True).data
        return Response(serializer)
