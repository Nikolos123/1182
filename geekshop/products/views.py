from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import os
import json

from products.models import Product,ProductsCategory

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# Контролер - функция

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request,id=None,page=1):

    products = Product.objects.get(category_id = id) if id != None else Product.objects.all().select_related('category')
    paginator = Paginator(products,per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {'title': 'Каталог',
               'category':  ProductsCategory.objects.all(),
               }
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)
