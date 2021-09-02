from django.shortcuts import render

import os
import json

from products.models import Product,ProductsCategory

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# Контролер - функция

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'Каталог',
               'products' : Product.objects.all(),
               'category':  ProductsCategory.objects.all(),
               }
    return render(request, 'products/products.html', context)
