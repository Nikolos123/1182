from django.contrib import admin

# Register your models here.
from baskets.models import Basket




# @admin.register(Basket)
# class BasketAdmin(admin.TabularInline):
#     fields = ('user','product','quantity','created_timestamp','update_timestamp')
#     readonly_fields = ('created_timestamp','update_timestamp')
#     # ordering = ('name','price')
#     # search_fields = ('name',)
