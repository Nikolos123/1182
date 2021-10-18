from django.core.management.base import BaseCommand
from products.models import Product
from  django.db import connection
from django.db.models import Q
from admins.views import db_profile_by_type

class Command(BaseCommand):
    def handle(self, *args, **options):
        products = Product.objects.filter(Q(category__name='Обувь') | Q(category__name='Подарки'))
        print(products)
        db_profile_by_type('learn db','',connection.queries)