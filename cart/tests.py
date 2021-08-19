import pytest
from pytest_django.asserts import assertContains
from shop.models import Product, Category
from cart.cart import Cart


# @pytest.fixture
# def product(db):
#     product = Product.objects.create(
#         category = Category.objects.create(
#         name = 'some_category'
#     ),
#         name = 'some tea',
#         slug = 'some-tea',
#         price = 30,
#         available = True
#     )
#     return product 

# def test_cart_add(db,product, request):
#     cart = Cart(request)
#     cart.add(product)
#     assert cart[1]

