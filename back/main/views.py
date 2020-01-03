from rest_framework.viewsets import ModelViewSet
from .serializers import WordSerializer
from .models import Word


class WordViewSet(ModelViewSet):
    model = 'main.Word'
    serializer_class = WordSerializer
    queryset = Word.objects.all()
