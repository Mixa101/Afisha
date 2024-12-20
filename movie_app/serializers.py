from rest_framework import serializers
from .models import Movie, Review, Director

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'director_', 'duration']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id' ,'text', 'movie', 'stars']
    
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
    
    def validate_title(self, value):
        if self.instance:
            if Movie.objects.filter(title=value).exclude(id=self.instance.id):
                raise serializers.ValidationError("Фильм с таким названием уже существует!")
            elif len(value) < 3:
                raise serializers.ValidationError("Название должно быть больше 3 символов")
        else:
            if Movie.objects.filter(title=value):
                raise serializers.ValidationError("Фильм с таким названием уже существует!")
        return value
    
    def validate_description(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("Описание не должно быть меньше 30 символов")
        return value
    
    def validate_duration(self, value):
        if value.total_seconds() < 1800:
            raise serializers.ValidationError("Продолжительность фильма должна быть не меньше 30 минут!")
        return value
  
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


# VALIDATORS
class DirectorValidateSerializer(DirectorSerializer):
    class Meta:
        model = Director
        fields = '__all__'
    name = serializers.CharField(min_length=5)