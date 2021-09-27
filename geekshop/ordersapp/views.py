from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView

from ordersapp.forms import OrderItemsForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView):
    model = Order
    # template_name = 'ordersappapp/order_list.html'
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(users=self.request.user)



class OrderCreate(CreateView):
    model = Order
    success_url = reverse_lazy('orders:list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
          formset = OrderFormSet()

        data['orderitems'] = formset

        return data


class OrderUpdate(UpdateView):
    pass


class OrderDelete(DeleteView):
    pass

class OrderRead(DetailView):
    pass


def forming_complete(request):
    pass