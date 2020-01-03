import json
import os

from django.conf import settings
from django.test import TestCase
from .models import Word

TEST_WORD_FIXTURE = {
    "word": "test",
    "id": 1,
    "sound": None,
}

# Create your tests here.
class GetWordsTestCase(TestCase):
    def test_get_a_word_using_id(self):
        word = Word.objects.create(word="test")
        TEST_WORD_FIXTURE['id'] = word.id

        resp = self.client.get(f'/api/word/{word.id}/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), TEST_WORD_FIXTURE)

    def test_get_a_words_list(self):
        word = Word.objects.create(word="test")
        TEST_WORD_FIXTURE['id'] = word.id

        resp = self.client.get(f'/api/word/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [TEST_WORD_FIXTURE]
        })

    def test_get_a_page_of_words(self):
        Word.objects.create(word="simple")
        word2 = Word.objects.create(word="test")

        TEST_WORD_FIXTURE['id'] = word2.id

        resp = self.client.get(f'/api/word/?limit=1&offset=1')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {
            "count": 2,
            "next": None,
            "previous": "http://testserver/api/word/?limit=1", # offset=0
            "results": [TEST_WORD_FIXTURE]
        })

class VoiceGenerationTestCase(TestCase):
    def test_generate_voice_over_aws_polly(self):
        word = Word.objects.create(word='test')

        from .actions import generate_voice
        word = generate_voice(word)

        self.assertIsNotNone(word.sound)
        try:
            self.assertEqual(
                word.sound.path,
                settings.MEDIA_ROOT + '/pronounciations/test.mp3'
            )
        finally:
            os.remove(word.sound.path)
