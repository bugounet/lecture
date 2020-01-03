import random
import boto3

from contextlib import closing
from django.core.files import File


def generate_voice(word):
    polly_generation_output = boto3.client('polly').synthesize_speech(
        OutputFormat='mp3',
        VoiceId=random.choice(['Mathieu', 'Lea']),
        Text=word.word
    )
    generated_sound_filename = f"{word.word}.mp3"
    with closing(polly_generation_output["AudioStream"]) as stream:
        polly_file = File(stream, generated_sound_filename)
        word.sound = polly_file
        word.save()
    return word