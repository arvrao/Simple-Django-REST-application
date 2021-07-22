from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Music(models.Model):
    song = models.TextField()
    place = models.CharField(max_length=130, null=True, blank=True)
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    genre = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music'
    
    def __str__(self):
        return self.song
    
