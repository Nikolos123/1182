from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from products.models import ProductsCategory, Product


class TestMainSmokeTest(TestCase):
    status_code_success = 200

    #1 предустановленные параметры
    def setUp(self) -> None:
        category = ProductsCategory.objects.create(name='Test')
        Product.objects.create(category=category,name='product_test',price=100)

        self.client = Client()

    #2 выполнения теста
    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,self.status_code_success)

    def test_products_product(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)

        # 2 выполнения теста
    def test_products_basket(self):
            response = self.client.get('/users/profile/')
            self.assertEqual(response.status_code, 302)

    #3 освобождения памяти от данных
    def tearDown(self) -> None:
        pass