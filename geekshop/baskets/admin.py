from django.contrib import admin

# Register your models here.
from baskets.models import Basket




class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product','quantity','created_timestamp','update_timestamp')
    readonly_fields = ('created_timestamp','update_timestamp')
    extra = 0

