from django.test import TestCase
from products.models import Product

from products.views import ProductGetAll

# Create your tests here.
class TestUrls(TestCase):

  def test_index(self):
    response = self.client.get('/products/')
    self.assertEqual(response.status_code,200)

    
    

