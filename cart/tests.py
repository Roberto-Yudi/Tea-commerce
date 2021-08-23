import pytest
from pytest_django.asserts import assertContains
from shop.models import Product, Category
from cart.cart import Cart

'''
@pytest.fixture
def product(db):
    product = Product.objects.create(
        category = Category.objects.create(
        name = 'some_category'
    ),
        name = 'some tea',
        slug = 'some-tea',
        price = 30,
        available = True
    )
    return product 

@pytest.fixture
def cart(db, request):
    cart = Cart(request)
    #cart = request.session.get('cart')
    # Session object has no atribute 'get' ??????
    return cart 

def test_cart_add(db, product, cart):
    cart.add(product)
    assert cart[1]

def test_cart_content(cart):
    cart.add(product, 2)
    assert cart.item['total_price'] == cart.item['price'] * cart.item['quantity']
'''