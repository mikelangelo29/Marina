from django.db import models
from django.urls import reverse


class News(models.Model):
    immagine=models.ImageField()
    titolo=models.CharField(max_length=150, default=None)
    descrizione=models.TextField()
    data_creazione= models.DateTimeField(auto_now_add=True)
    firma= models.CharField(max_length=30, default=None)
    
    class Meta:
        ordering=['-data_creazione']

    def __str__(self):
        return self.titolo
    
