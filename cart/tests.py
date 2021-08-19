from django.http import request
import pytest
from pytest_django.asserts import assertContains
from shop.models import Product
from cart.cart import Cart

# @pytest.fixture
# def sample_product(db):
#     product = Product.objects.get()
#     return product


# def test_cart_add(db,sample_product):
#     cart = Cart(request)
#     cart.add(sample_product)
#     assert cart[1]

