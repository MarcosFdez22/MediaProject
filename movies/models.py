from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mediaproject/images',blank=True) 
    description = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title