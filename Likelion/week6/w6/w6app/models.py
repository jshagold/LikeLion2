from django.db import models
from django.utils.timezone import now

# Create your models here.
class Playlist(models.Model) :
    CHOICES = (
        ('H', '힙합'),
        ('B', '벌러두'),
        ('D', '댄스')
    )

    title = models.CharField(max_length=20)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=20, choices = CHOICES)
    lyrics = models.TextField()
    release = models.DateTimeField(default=now)
    composer = models.CharField(max_length=20, default='작사가없음')
    lyricist = models.CharField(max_length=20, default='작곡가없음')


    def __str__(self):
        return self.title