from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock', 'image']
        labels = {
            'name': 'Nome',
            'category': 'Categoria',
            'price': 'Valor unitário',
            'stock': 'Estoque',
            'image': 'Imagem'
        }
