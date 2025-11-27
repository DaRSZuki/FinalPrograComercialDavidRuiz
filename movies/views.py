from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def movie_list(request):
    """
    Endpoint 1: Lista todas las películas
    GET /api/movies/
    """
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movies_by_category(request, category):
    """
    Endpoint 2: Filtra películas por categoría
    GET /api/movies/category/<category>/
    """
    movies = Movie.objects.filter(category=category)
    
    if not movies.exists():
        return Response(
            {'error': f'No se encontraron películas de la categoría: {category}'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)