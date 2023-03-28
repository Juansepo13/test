from django.db import models

# Create your models here.

class Pokemon(models.Model):
    # pokemon es una subclase de models.Model
    # trata de un modelo de datos que se almacenara 
    # en la base de datos
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    variable = models.CharField(max_length=100)

    # metodo __str__  utilizado por Django para representar 
    # los objetos de este modelo en la consola 
    # de administración de Django
    def __str__(self):
        return self.name
