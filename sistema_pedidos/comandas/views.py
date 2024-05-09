from django.shortcuts import render, redirect
from .models import Barraca, Item, OperadorBarraca, Pedido, ItemPedido
from .forms import ItemPedidoForm, BarracaForm, PedidoForm, ItemForm, ItemPedidoFormSet, ItemFormSet, BarracaFormSet

# Create your views here.
def index(request):
    return render(request, 'comandas/index.html')

def lista_barracas(request):
    barracas = Barraca.objects.all()
    return render(request, 'comandas/lista_barracas.html', {'barracas': barracas})

def lista_itens_por_barraca(request, barraca_id):
    barraca = Barraca.objects.get(id=barraca_id)
    itens = Item.objects.filter(barraca=barraca)
    return render(request, 'comandas/lista_itens.html', {'itens': itens, 'barraca': barraca})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'comandas/lista_pedidos.html', {'pedidos': pedidos})

def criar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item_criado = form.save()
            return redirect('lista_itens', barraca_id=item_criado.barraca.id)
    else:
        form = ItemForm()
    return render(request, 'comandas/criar_item.html', {'form': form})


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