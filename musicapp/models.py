from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    songs = models.ForeignKey("Song", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.first_name
    
    
class Song(models.Model):
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    likes = models.BooleanField()
    lyrics = models.ForeignKey("Lyric", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    
class Lyric(models.Model):
    song_id = models.AutoField(primary_key=True)
    content = models.TextField()
    
    def __str__(self):
            return str(self.song_id)
