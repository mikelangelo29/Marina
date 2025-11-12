from django.db import models

# Create your models here.

class Hotel(models.Model):
    immagine=models.ImageField()
    titolo=models.CharField(max_length=50, default=None)
    descrizione=models.CharField(max_length=250, default=None)
    item1=models.CharField(max_length=250, default=None)
    
 

    def __str__(self):
        return self.titolo
    
class Risto (models.Model):
    immagine=models.ImageField()
    titolo=models.CharField(max_length=50, default=None)
    descrizione=models.CharField(max_length=250, default=None)
    item1=models.CharField(max_length=250, default=None)


    def __str__(self):
        return self.titolo
    

class Spiagge (models.Model):
    immagine=models.ImageField()
    titolo=models.CharField(max_length=50, default=None)
    descrizione=models.CharField(max_length=250, default=None)
    item1=models.CharField(max_length=250, default=None)
    

    def __str__(self):
        return self.titolo
    