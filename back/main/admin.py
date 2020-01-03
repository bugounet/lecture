from django.contrib import admin
from .models import Word
from .actions import generate_voice


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    class Meta:
        model = 'main.Word'

    actions = ['generate_voice']

    def generate_voice(self, request, objects):
        for word in objects:
            generate_voice(word)
