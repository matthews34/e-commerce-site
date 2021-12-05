from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from .forms import ProductForm
from .models import Product

# Create your views here.

def register_product(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:list_products'))

    context = {
        'form': form
    }
    return render(request, 'website/register_product.html', context)

def list_products(request):
    products = get_list_or_404(Product)
    context = {
        'products': products
    }
    return render(request, 'website/list_products.html', context)

def detail_product(request, id):
    context = {
        'product': get_object_or_404(Product, id=id)
    }
    return render(request, 'website/detail_product.html', context)

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:list_products'))

    context = {
        'product': product,
        'form': form
    }
        
    return render(request, 'website/update_product.html', context)

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }

    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect(reverse('website:list_products'))

    return render(request, 'website/delete_product.html')

        
def index(request):
    return HttpResponse('Index')
