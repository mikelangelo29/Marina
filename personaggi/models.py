from django.db import models

# Create your models here.

class Personaggi (models.Model):
    immagine=models.ImageField()
    titolo=models.CharField(max_length=50, default=None)
    descrizione=models.CharField(max_length=150, default=None)
    item1=models.TextField(default=None)
    
    def __str__(self):
        return self.titolo