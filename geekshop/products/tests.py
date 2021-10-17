from django.test import TestCase
from products.models import ProductsCategory, Product
from django.test.client import Client


class TestMainSmokeTest(TestCase):

    def setUp(self):
        category = ProductsCategory.objects.create(
            name='TestCat1'
        )
        Product.objects.create(
            category=category,
            name='product_test_1',
            price=100
        )
        self.client = Client()
    def tearDown(self):
        #определяется для очистки после
        # работы теста исполяется после setUP
        # (базу удалять не нужно она автоматом удалится)
        # но данные чистим допустим когда мы выкачивали
        # аватар на первом уроке ее можно почистить
        #но очень редко сам использую и коллеги тоже
        pass

    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_products_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, 200)

