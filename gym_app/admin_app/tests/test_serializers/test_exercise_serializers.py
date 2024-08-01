import pytest
from gym_app.admin_app.models import Exercise
from gym_app.admin_app.serializers import ExerciseSerializer
from datetime import datetime


@pytest.mark.django_db()
class TestExerciseSerializer:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.exercise = Exercise.objects.create(name="Bench Press", target_area="CHEST")
        self.exercise_serializer = ExerciseSerializer

    def test_exercise_serializer_data(self):
        exercise_serializer = self.exercise_serializer(self.exercise)

        assert exercise_serializer.data["id"] == self.exercise.id
        assert exercise_serializer.data["name"] == "Bench Press"
        assert exercise_serializer.data["target_area"] == "CHEST"
        assert exercise_serializer.data["date_added"] == datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
