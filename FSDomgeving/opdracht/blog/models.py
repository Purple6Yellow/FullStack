from django.conf import settings
from django.db import models
from django.utils import timezone

#object georienteerd programmeren > defnieert objecten. Objecten zijn exemplaren van klasse. Per object dient u dezelfde velden (eigenschappen/gedragingen)
# in te vullen 

# klasse > class = Post 
# eigenschappen:    Datum / Tijdstip (begin en eind) / Omschrijving / Kosten

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank = True, null = True)
    end_time = models.TimeField(blank = True, null = True)
    text = models.TextField()
    prijs = models.IntegerField() 

    def Welkenaam(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
