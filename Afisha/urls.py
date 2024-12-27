from django.contrib import admin
from django.urls import path, include
from movie_app.views import *
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', include('movie_app.urls')),
    path('api/v1/users/', include('users.urls')),
]

urlpatterns += swagger.urlpatterns