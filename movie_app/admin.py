from django.contrib import admin
from .models import Review, Movie, Director

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)