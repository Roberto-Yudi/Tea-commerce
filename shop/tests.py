import pytest
from model_bakery import baker
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed
from django.test import Client
from django.urls import reverse, resolve
from .views import product_list

from .models import Category, Product

class Test_Product:

    @pytest.fixture
    def product(self, db):
        return baker.make(Product)
    
    def test_product_list_view(self, client, product, db):

        response = client.get(reverse('shop:product_list'))
        view = resolve('/')

        assert response.status_code == 200
        assert view.func.__name__ == product_list.__name__
        assertContains(response, product.name)
        assertContains(response, product.category)
        # assertContains(response, product.price)
        assertContains(response, product.get_absolute_url())
        assertNotContains(response, 'should not be on the page')
        assertTemplateUsed(response, 'shop/product/list.html')
 

    def test_product_detail_view(self, product, client, db):

        response = client.get(product.get_absolute_url())
        # view = resolve(f'{product.id}/{product.slug}/')

        assert response.status_code == 200
        # assert view.func.__name__ == product_detail.__name__
        assertContains(response, product.name)
        assertContains(response, product.category)
        assertNotContains(response, 'should not be on the page')
        assertTemplateUsed(response, 'shop/product/detail.html')


