from django.db import models

# Create your models here.

class fooddata(models.Model):
    Breakfast=models.CharField(max_length=100)
    Protein=models.IntegerField()


    class Meta:
         verbose_name_plural ='Calorie meter'

def __str__(self):
    return f'{self.breakfast}-{self.lunch}'

