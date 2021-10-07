from django.contrib import admin
from django.urls import path

app_name = 'ordersapp'

from .views import OrderCreate,OrderList,OrderRead,OrderUpdate,OrderDelete,order_forming_complete,payment_result,get_product_price

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('read/<int:pk>/', OrderRead.as_view(), name='read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('forming-complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('product/<int:pk>/price/',get_product_price,name='product_price'),

    path('payment/result/',payment_result,name='payment_result')
]
