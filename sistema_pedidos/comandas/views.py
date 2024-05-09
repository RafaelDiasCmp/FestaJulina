from django.shortcuts import render, redirect
from .models import Barraca, Item, OperadorBarraca, Pedido, ItemPedido
from .forms import ItemPedidoForm, BarracaForm, PedidoForm, ItemForm, ItemPedidoFormSet, ItemFormSet, BarracaFormSet

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
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_itens')
    else:
        form = ItemForm()
        formset = ItemFormSet()
    return render(request, 'comandas/criar_item.html', {'form': form, 'formset': formset})

def criar_barraca(request):
    if request.method == 'POST':
        form = BarracaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_barracas')
    else:
        form = BarracaForm()
        formset = BarracaFormSet()

    return render(request, 'comandas/criar_barraca.html', {'form': form, 'formset': formset})

def criar_pedido(request):
    return render(request, 'comandas/criar_pedido.html')