from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    barraca = models.ForeignKey('Barraca', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


    def __str__(self):
        return self.user.username

class Barraca(models.Model):
    """ Barraca que vende itens """
    nome = models.CharField(max_length=100)
    


class OperadorBarraca(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    barraca = models.ForeignKey(Barraca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    barraca = models.ForeignKey(Barraca, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pedido {self.id}'


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} de {self.item.nome}'
    
