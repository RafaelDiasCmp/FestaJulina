from django.shortcuts import render
from .models import Barraca, Item, OperadorBarraca, Pedido, ItemPedido

# Create your views here.
def index(request):
    return render(request, 'comandas/index.html')

def lista_barracas(request):
    barracas = Barraca.objects.all()
    return render(request, 'comandas/lista_barracas.html', {'barracas': barracas})

def lista_itens(request):
    itens = Item.objects.all()
    return render(request, 'comandas/lista_itens.html', {'itens': itens})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'comandas/lista_pedidos.html', {'pedidos': pedidos})

def criar_item(request):
    return render(request, 'comandas/criar_item.html')

def criar_barraca(request):
    return render(request, 'comandas/criar_barraca.html')

def criar_pedido(request):
    return render(request, 'comandas/criar_pedido.html')