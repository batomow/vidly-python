from django.contrib import admin
from .models import Genere, Movie

class GenereAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin): 
    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate')

# Register your models here.
admin.site.register(Genere, GenereAdmin)
admin.site.register(Movie, MovieAdmin)