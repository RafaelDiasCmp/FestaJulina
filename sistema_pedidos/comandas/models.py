from django.db import models

# Create your models here.

class Comanda(models.Model):
    cliente = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
    

class Barraca(models.Model):
    nome = models.CharField(max_length=100)
    comandas = models.ManyToManyField(Comanda)

    def __str__(self):
        return self.nome