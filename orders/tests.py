import pytest
from model_mommy import mommy
from pytest_django.asserts import assertContains
from .forms import OrderCreateForm
from .models import Order

@pytest.fixture
def order(db):
    order = mommy.make(Order)
    return order

def test_order_model(order):
   assert Order.first_name 
   assert Order.last_name 
   assert Order.email 
   assert Order.address
   assert Order.postal_code 
   assert Order.city 
   assert Order.created 
   assert Order.updated 
   assert Order.paid

    


