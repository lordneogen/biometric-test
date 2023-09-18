from django.db import models

# Create your models here.
class Persons(models.Model):  
        
    iin = models.IntegerField(primary_key=True)
    
    name = models.TextField(null=False)
    
    age = models.IntegerField(null=True)

    def __str__(self):
        return str(self.iin)

    class Meta:

        managed = True
        db_table = 'persons'
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'
