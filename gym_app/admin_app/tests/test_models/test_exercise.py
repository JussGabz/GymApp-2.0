import pytest
from gym_app.admin_app.models import Exercise
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestExerciseModel:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.exercise = Exercise.objects.create(name="Bench Press", target_area="CHEST")
        self.exercise.save()

    def test_exercise_name(self):
        assert self.exercise.name == "Bench Press"

    def test_exercise_target_area(self):
        assert self.exercise.target_area == "CHEST"

    def test_exercise_date_added(self):
        assert self.exercise.date_added is not None

    def test_exercise_wrong_target_area(self):
        self.exercise.target_area = "EAR"
        with pytest.raises(ValidationError) as e_info:
            self.exercise.save()
