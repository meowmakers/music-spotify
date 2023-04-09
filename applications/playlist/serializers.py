from .models import Song, Genre, Album, Like
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(method_name='likes_counter')
        
    class Meta:
        model = Song
        fields = '__all__'
    
    def likes_counter(self, instance):
        return Like.objects.filter(Song=instance).count()
    

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre 
        fields = ['id', 'title']
        

class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = '__all__'