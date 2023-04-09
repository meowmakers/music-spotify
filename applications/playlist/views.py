from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response 
from .serializers import SongSerializer, AlbumSerializer, GenreSerializer
from .models import Song, Album, Genre, Like

# Create your views here.

class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        Song = self.get_object()
        like = Like.objects.filter(user=request.user, Song=Song)
        if like.exists():
            like.delete()
            return Response({'Liked': False})
        else: 
            Like.objects.create(user=request.user, Song=Song).save()
            return Response({'Liked': True})
    
class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer