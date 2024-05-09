from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK


class CreateProductTestCase(TestCase):
    url = reverse('product_create')

    def setup(self):
        self.user = User.objects.create(username='username1', password='1q2w3e4r')
        self.user_token = Token.objects.get_or_create(user=self.user)[0]
        self.headers = {'Authorization': f'Token {self.user_token}'}

    def test_create_product_ok(self):
        new_product = {
            'name': 'Product',
            'description': 'A product',
            'price': 10,
            'weight': 10,
            'volume': 10,
        }

        response = self.client.post(self.url, data=new_product, headers=self.headers)

        self.assertEqual(response.status_code, HTTP_200_OK)
