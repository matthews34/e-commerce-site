from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock', 'image']
        labels = {
            'name': 'Nome',
            'category': 'Categoria',
            'price': 'Preço unitário',
            'stock': 'Quantidade em estoque',
            'image': 'Imagem'
        }
