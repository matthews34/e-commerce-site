from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

from .forms import ProductForm
from .models import Product

# Create your views here.

class RegisterProduct(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'website/register_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:index'))
        
def index(request):
    return HttpResponse('Index')
