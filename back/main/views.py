from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import WordSerializer
from .models import Word


class WordViewSet(ModelViewSet):
    model = 'main.Word'
    serializer_class = WordSerializer
    queryset = Word.objects.all()

    @action(detail=False)
    def random(self, request):
        random_words = Word.objects.all().order_by('?')

        page = self.paginate_queryset(random_words)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(random_words, many=True)
        return Response(serializer.data)
