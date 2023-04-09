from django.contrib import admin
from .models import Song, Album, Genre, Like

# Register your models here.

admin.site.register([Song, Album, Genre, Like])