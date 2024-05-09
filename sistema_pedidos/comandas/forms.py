from django import forms
from .models import ItemPedido,Item,Barraca, Pedido

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['item', 'quantidade']
        labels = {
            'item': 'Item',
            'quantidade': 'Quantidade',
        }
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BarracaForm(forms.ModelForm):
    class Meta:
        model = Barraca
        fields = ['nome', 'responsavel']
        labels = {
            'nome': 'Nome',
            'responsavel': 'Responsável',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['barraca']
        labels = {
            'barraca': 'Barraca',
        }
        widgets = {
            'barraca': forms.Select(attrs={'class': 'form-control'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'valor', 'barraca']
        labels = {
            'nome': 'Nome',
            'valor': 'Valor',
            'barraca': 'Barraca',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control'}),
            'barraca': forms.Select(attrs={'class': 'form-control'}),
        }

ItemPedidoFormSet = forms.inlineformset_factory(Pedido, ItemPedido, form=ItemPedidoForm, extra=1)

ItemFormSet = forms.inlineformset_factory(Barraca, Item, form=ItemForm, extra=1)

BarracaFormSet = forms.inlineformset_factory(Barraca, Item, form=ItemForm, extra=1)