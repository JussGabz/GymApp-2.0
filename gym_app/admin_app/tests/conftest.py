import pytest 
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from ..models import Exercise, WorkoutPlan
from django.utils import timezone, dateformat


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
    exercise = Exercise.objects.create(
        name="test_exercise",
        target_area="test_target_area",
    )
    return exercise

@pytest.fixture
def test_workout_plan(db):
    workoutplan = WorkoutPlan.objects.create(
        name="test_workout_plan",
        workout_type="test_type",
    )
    return workoutplan

@pytest.fixture
def create_api_object():
    """
    Helper function to create an API object via a POST request.

    Args:
        api_client (APIClient): The Django REST framework test client.
        api_endpoint (str): The API endpoint to send the POST request.
        request_data (dict): The data to be sent in the POST request.

    Returns:
        Response: The response object from the API call.

    """

    def _create_api_object(api_client, api_endpoint, request_data):
        return api_client.post(api_endpoint, request_data, format='json')

    return _create_api_object

