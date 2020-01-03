from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=50, unique=True)
    sound = models.FileField(upload_to='pronounciations', blank=True, null=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"[{self.id}] {self.word}"
