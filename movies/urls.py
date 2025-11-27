from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list, name='movie-list'),
    path('movies/category/<str:category>/', views.movies_by_category, name='movies-by-category'),
]