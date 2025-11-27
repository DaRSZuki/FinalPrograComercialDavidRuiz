from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'rating', 'release_year', 'duration_minutes']
    list_filter = ['category', 'release_year']
    search_fields = ['title']