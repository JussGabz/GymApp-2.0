import pytest 
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import Exercise


User = get_user_model()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username="JussGabz", email="admin@jussgym.com")
    return user

@pytest.fixture
def api_client(test_user):
    client = APIClient()
    client.force_authenticate(test_user)
    return client

@pytest.fixture
def test_exercise(db, test_user):
    exercise = Exercise.objects.get_or_create(
        name="test_exercise",
        target_area="test_target_area",
    )

    return exercise
