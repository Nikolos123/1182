from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
import json

from products.models import Product,ProductsCategory

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# Контролер - функция

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request,id=None):
    # products_filter =

    # if id != None:
    #     products_filter = Product.objects.filter(category_id = id)
    # else:
    #     products_filter = Product.objects.all()
    context = {'title': 'Каталог',
               'category':  ProductsCategory.objects.all(),
               }
    # context['products'] = products_filter
    context.update({'products': Product.objects.filter(category_id = id)  if id != None  else Product.objects.all() })
    return render(request, 'products/products.html', context)
