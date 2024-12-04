from django.contrib import admin
from django.urls import path, include
from movie_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
]
