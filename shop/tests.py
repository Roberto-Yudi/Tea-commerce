from django.test import TestCase
from .models import Category, Product
import pytest

class Test_Product:

    @pytest.fixture
    def product(self, db):
        product = Product.objects.create(
            category = Category.objects.create(
            name = 'some_category'
        ),
            name = 'some_tea',
            price = '30',
            available = True
        )
        return product 
    
    def test_product_creation(self, product):
        assert product.name == 'some_tea'
        assert product.price == '30'
        assert product.available
