from rest_framework.routers import DefaultRouter
from .views import WordViewSet


router = DefaultRouter()
router.register('word', WordViewSet, basename='word')

urlpatterns = (router.urls, 'main')
