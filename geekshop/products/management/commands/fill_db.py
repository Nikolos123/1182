import json
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from products.models import ProductsCategory, Product

JSON_PATH = 'products/fixtures'


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='windows-1251') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('products/fixtures/category.json')

        ProductsCategory.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductsCategory(**cat)
            new_category.save()

        products = load_from_json('products/fixtures/products.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductsCategory.objects.get(id=category)
            prod['category'] =_category
            new_category = Product(**prod)
            new_category.save()

        # super_user = User.objects.create_superuser('nikolay','test@mail.ru','1')