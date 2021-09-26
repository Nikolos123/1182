from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

import os
import json

from django.views.generic import DetailView

from products.models import Product,ProductsCategory

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# Контролер - функция

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request,id=None,page=1):

    products = Product.objects.filter(category_id = id) if id != None else Product.objects.all()
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



class ProductDetail(DetailView):
    """
    Контроллер вывода информации о продукте
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, category_id=None, *args, **kwargs):
        """Добавляем список категорий для вывода сайдбара с категориями на странице каталога"""
        context = super().get_context_data()
        context['categories'] = ProductsCategory.objects.all()
        return context