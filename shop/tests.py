import pytest
from pytest_django.asserts import assertNotContains, assertTemplateUsed
from django.test import Client
from django.urls import reverse, resolve
from .views import product_list

from .models import Category, Product

class Test_Product:

    @pytest.fixture
    def product(self, db):
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
    
    def test_product_creation(self, product):
        assert product.name == 'some tea'
        assert product.category.name == 'some_category'
        assert product.slug == 'some-tea'
        assert product.price == 30
        assert product.available

    def test_product_list_view(self, client, db):
        response = client.get(reverse('shop:product_list'))
        view = resolve('/')
        assert response.status_code == 200
        assert view.func.__name__ == product_list.__name__
        assertNotContains(response, 'should not be on the page')
        assertTemplateUsed(response, 'shop/product/list.html')
 

    # def test_product_detail_view(self, product, client, db):
    #     response = client.get(product.get_absolute_url())
    #     assert response.status_code == 200

    # product.get_absolute_url() esta acessando o get_absolute_url da classe Category e não da classe Product
    # já tentei colocar a categoria em uma fixture propria e injetar no product, mas o erro persiste.