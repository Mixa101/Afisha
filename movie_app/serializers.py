from rest_framework import serializers
from .models import Movie, Review, Director

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'director']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie']
        

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
  
class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
  
class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ["id","name", "movies_count", "movies_names"]

class MoviesReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'reviews_', 'average_rate']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id' ,'name', 'movies_count']
