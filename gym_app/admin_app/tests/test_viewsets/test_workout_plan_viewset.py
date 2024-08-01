from rest_framework.test import APIClient
from gym_app.admin_app.models import WorkoutPlan
from django.urls import reverse
import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestWorkoutPlanViewSet:

    def setup(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(username="temp_user", password="temp_pass")
        self.workoutplan = WorkoutPlan.objects.create(
            name="Strength Workout", workout_type="CARDIO", created_by=self.user
        )

    def test_workoutplan_list(self):

        url = reverse("workoutplan-list")

        response = self.api_client.get(url)
        assert response.status_code == 200
        assert response.data["results"][0]["name"] == "Strength Workout"

    def test_workout_plan_detail(self):
        url = reverse("workoutplan-detail", kwargs={"pk": self.workoutplan.id})

        response = self.api_client.get(url)
        assert response.status_code == 200
        assert response.data["name"] == "Strength Workout"

    def test_workout_plan_update(self):
        url = reverse("workoutplan-detail", kwargs={"pk": self.workoutplan.id})
        data = {"name": "New Strength Workout", "workout_type": "HIIT"}
        self.api_client.force_login(user=self.user)
        response = self.api_client.put(url, data, format="json")
        assert response.status_code == 200
        self.workoutplan.refresh_from_db()
        assert self.workoutplan.name == "New Strength Workout"
        assert self.workoutplan.workout_type == "HIIT"

    def test_workout_plan_delete(self):
        url = reverse("workoutplan-detail", kwargs={"pk": self.workoutplan.id})

        self.api_client.force_login(user=self.user)
        response = self.api_client.delete(url)
        assert response.status_code == 204
