from django.conf import settings
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from products.models import ProductsCategory, Product
from users.models import User


class TestMainSmokeTest(TestCase):
    status_code_success = 200
    status_code_render = 302
    username = 'django'
    email = 'django@mail.ru'
    password = 'geekbrains'

    new_user_data = {
        'username':'django1',
        'first_name':'Django',
        'last_name': 'Django2',
        'password1': 'geekbrains',
        'password2': 'geekbrains',
        'email': 'djang111o@mail.ru',

    }

    #1 предустановленные параметры
    def setUp(self) -> None:
        self.user = User.objects.create_superuser(self.username,email=self.email,password=self.password)
        self.client = Client()

    #2 выполнения теста
    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,self.status_code_success)

        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.username,password=self.password)
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, self.status_code_render)

    def test_register(self):
        response = self.client.post('/users/register/',data=self.new_user_data)
        self.assertEqual(response.status_code,self.status_code_render)


        new_user = User.objects.get(username=self.new_user_data['username'])
        print(new_user)
        #готовим ссылку
        activation_url = f"{settings.DOMAIN_NAME}/users/verify/{self.new_user_data['email']}/{new_user.activation_key}/"
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, self.status_code_success)

        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)


    #3 освобождения памяти от данных
    def tearDown(self) -> None:
        pass