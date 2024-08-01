import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from gym_app.admin_app.models import WorkoutPlan
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestWorkoutFilter:

    def setup(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(username="temp_user", password="temp_pass")

        WorkoutPlan.objects.create(
            name="Test WorkoutPlan 1", workout_type="CARDIO", created_by=self.user
        )
        WorkoutPlan.objects.create(
            name="Test WorkoutPlan 2", workout_type="HIIT", created_by=self.user
        )
        WorkoutPlan.objects.create(
            name="Test WorkoutPlan 3", workout_type="CARDIO", created_by=self.user
        )

    def test_workout_type_filter(self):
        url = reverse("workoutplan-list")
        response = self.api_client.get(url, {"workout_type": "CARDIO"})
        print(response.data)
        assert response.status_code == 200
        assert response.data["count"] == 2
        assert response.data["results"][0]["name"] == "Test WorkoutPlan 1"
        assert response.data["results"][1]["name"] == "Test WorkoutPlan 3"
