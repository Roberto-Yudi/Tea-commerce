from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CustomUser

def test_user_model_used():
    assert get_user_model() == CustomUser
