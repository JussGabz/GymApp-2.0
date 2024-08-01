from rest_framework.test import APIClient
from gym_app.admin_app.models import Exercise
from django.urls import reverse
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestExerciseViewSet:

    def setup(self):
        self.exercise = Exercise.objects.create(name="Bench Press", target_area="CHEST")
        self.user = User.objects.create_user(username="temp_user", password="temp_pass")

    def test_exercises_list_authenticated_user(self, api_client):

        url = reverse("exercise-list")
        api_client.force_login(self.user)
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["results"][0]["name"] == "Bench Press"

    def test_exercise_detail_authenticated_user(self, api_client):
        url = reverse("exercise-detail", kwargs={"pk": self.exercise.id})
        api_client.force_login(self.user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_exercise_update_authenticated_user(self, api_client):
        url = reverse("exercise-detail", kwargs={"pk": self.exercise.id})
        data = {"name": "Updated Exercise", "target_area": "BACK"}

        api_client.force_login(user=self.user)
        response = api_client.put(url, data, format="json")

        assert response.status_code == 403


    def test_exercise_delete_authenticated_user(self, api_client):
        url = reverse("exercise-detail", kwargs={"pk": self.exercise.id})

        api_client.force_login(user=self.user)
        response = api_client.delete(url)

        assert response.status_code == 403
