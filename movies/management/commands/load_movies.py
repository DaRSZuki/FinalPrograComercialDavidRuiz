from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Carga películas de prueba en la base de datos'

    def handle(self, *args, **kwargs):
        Movie.objects.all().delete()
        
        movies_data = [
            # Acción
            {'title': 'Mad Max: Fury Road', 'category': 'Acción', 'rating': 8.1, 'release_year': 2015, 'duration_minutes': 120},
            {'title': 'John Wick', 'category': 'Acción', 'rating': 7.4, 'release_year': 2014, 'duration_minutes': 101},
            {'title': 'Die Hard', 'category': 'Acción', 'rating': 8.2, 'release_year': 1988, 'duration_minutes': 132},
            
            # Drama
            {'title': 'El Padrino', 'category': 'Drama', 'rating': 9.2, 'release_year': 1972, 'duration_minutes': 175},
            {'title': 'Forrest Gump', 'category': 'Drama', 'rating': 8.8, 'release_year': 1994, 'duration_minutes': 142},
            {'title': 'Cadena Perpetua', 'category': 'Drama', 'rating': 9.3, 'release_year': 1994, 'duration_minutes': 142},
            
            # Comedia
            {'title': 'Mi Pobre Angelito', 'category': 'Comedia', 'rating': 7.7, 'release_year': 1990, 'duration_minutes': 103},
            {'title': 'Superbad', 'category': 'Comedia', 'rating': 7.6, 'release_year': 2007, 'duration_minutes': 113},
            {'title': 'Loco por Mary', 'category': 'Comedia', 'rating': 7.1, 'release_year': 1998, 'duration_minutes': 119},
            
            # Ciencia Ficción
            {'title': 'Inception', 'category': 'Ciencia Ficción', 'rating': 8.8, 'release_year': 2010, 'duration_minutes': 148},
            {'title': 'Matrix', 'category': 'Ciencia Ficción', 'rating': 8.7, 'release_year': 1999, 'duration_minutes': 136},
            {'title': 'Interestelar', 'category': 'Ciencia Ficción', 'rating': 8.6, 'release_year': 2014, 'duration_minutes': 169},
        ]
        
        for movie_data in movies_data:
            Movie.objects.create(**movie_data)
        
        self.stdout.write(self.style.SUCCESS(f'Se cargaron {len(movies_data)} películas exitosamente'))