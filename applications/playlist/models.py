from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/album_images', null=True, blank=True)
    release_date = models.DateTimeField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField("Genre", related_name='albums')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = "Альбомы"
        ordering = ['uploaded_at']

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)
    duration = models.PositiveIntegerField(help_text='Duration in seconds')
    release_date = models.DateField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    genre = models.ManyToManyField("Genre", related_name='songs')
    
    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = "Песни"
        ordering = ['uploaded_at']

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.album})"

class Genre(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    track = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ['user', 'track']

    def __str__(self):
        return f'Liked by {self.user.username}'