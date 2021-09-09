from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Basket
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from django.http import JsonResponse


@login_required
def baskets_add(request, id):
    product = Product.objects.get(id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/baskets.html', context)
        return JsonResponse({'result': result})
