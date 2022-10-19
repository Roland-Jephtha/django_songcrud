from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    like = models.CharField(max_length=255)
    songs = models.ForeignKey("Song", on_delete=models.CASCADE)
    
    
class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.BooleanField()
    lyrics = models.ForeignKey("Lyric", on_delete=models.CASCADE)

    
class Lyric(models.Model):
    song_id = models.AutoField(primary_key=True)
    content = models.TextField()
