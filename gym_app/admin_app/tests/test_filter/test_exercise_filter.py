import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from gym_app.admin_app.models import Exercise
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestExerciseFilter:

    def setup(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user("Test User", "user@jussgym.com")

        Exercise.objects.create(name="Test Exercise 1", target_area="CHEST")
        Exercise.objects.create(name="Test Exercise 2", target_area="BACK")
        Exercise.objects.create(name="Test Exercise 3", target_area="CHEST")

    def test_target_area_filter(self):
        url = reverse("exercise-list")
        self.api_client.force_login(self.user)
        response = self.api_client.get(url, {"target_area": "CHEST"})

        assert response.status_code == 200
        assert response.data["count"] == 2
        assert response.data["results"][0]["name"] == "Test Exercise 1"
        assert response.data["results"][1]["name"] == "Test Exercise 3"
