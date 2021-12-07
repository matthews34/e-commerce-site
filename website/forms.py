from django import forms
from crispy_forms.helper import FormHelper

from .models import Product

class ProductForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    helper = FormHelper()
    
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
