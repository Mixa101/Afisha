from rest_framework import serializers
from .models import Movie, Review, Director

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'director_', 'duration']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'movie', 'stars']
    
    # в случае вывода исключаем stars
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('stars', None)
        return data
    
        

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
