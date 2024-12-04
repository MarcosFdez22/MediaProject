from django.db import models

# Create your models here.

class Serie(models.Model): 
    title = models.CharField(max_length=50,blank=True) 
    image = models.ImageField(upload_to='mediaproject/images',blank=True) 
    chapters = models.CharField(max_length=100,blank=True) 
    description = models.CharField(max_length=2000, blank=True) 
    puntuation = models.IntegerField(blank=True, default=0) 
    
    def __str__(self): return self.title