from rest_framework.routers import DefaultRouter 
from .views import SongViewSet, AlbumViewSet, GenreViewSet


router = DefaultRouter()
router.register('song', SongViewSet, 'songs')
router.register('album', AlbumViewSet, 'albums')
router.register('genre', GenreViewSet, 'genres')


urlpatterns = router.urls