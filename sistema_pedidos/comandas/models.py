from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comanda(models.Model):
    cliente = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
    

class Item(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    def __str__(self):
        return self.user.username

class Barraca(models.Model):
    nome = models.CharField(max_length=100)
    comandas = models.ManyToManyField(Comanda)


class OperadorBarraca(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    barraca = models.ForeignKey(Barraca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome