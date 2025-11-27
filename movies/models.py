from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('Acción', 'Acción'),
        ('Drama', 'Drama'),
        ('Comedia', 'Comedia'),
        ('Ciencia Ficción', 'Ciencia Ficción'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)]
    )
    release_year = models.IntegerField()
    duration_minutes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'