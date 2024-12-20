from .models import Movie, Review, Director
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .serializers import *


# views for get all models objects in one JSON

# THIS FOR LIST OF MOVIES
class MoviesList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = MovieDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# THIS FOR LIST OF REVIEWS
class ReviewsList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def create(self, request, *args, **kwargs):
        # Легче все сделать через сериализатор
        print(request.data)
        serializer = ReviewDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# THIS FOR LIST OF DIRECTORS
class DirectorsList(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    
    def create(self, request, *args, **kwargs):
        new_director = DirectorValidateSerializer(data=request.data)
        
        if new_director.is_valid():
            new_director.save()
            return Response(data=new_director.data, status=status.HTTP_201_CREATED)
        return Response(new_director.errors, status=status.HTTP_400_BAD_REQUEST)


# THIS FOR DETAIL OF MOVIE
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    

# THIS FOR DETAIL OF REVIEW
class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    
# THIS FOR DETAIL OF DIRECTOR
class DirectorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DirectorDetailSerializer
        return DirectorValidateSerializer
    

# THIS FOR MOVIES WITH THEIR REVIEWS
class MoviesReviewsList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MoviesReviewsSerializer(movies, many=True).data
        return Response(serializer)
