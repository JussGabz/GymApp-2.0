import pytest
from gym_app.admin_app.models import WorkoutPlan, Exercise
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestWorkoutPlan:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user = User.objects.create(username="Test User")
        self.workout_plan = WorkoutPlan.objects.create(
            name="Test Work Out Plan", workout_type="CARDIO", created_by=self.user
        )
        self.exercise = Exercise.objects.create(name="Bench Press", target_area="CHEST")
        self.workout_plan.save()

    def test_workout_plan_name(self):
        assert self.workout_plan.name == "Test Work Out Plan"

    def test_workout_plan_workout_type(self):
        assert self.workout_plan.workout_type == "CARDIO"

    def test_workout_plan_date_added(self):
        assert self.workout_plan.date_added is not None

    def test_workout_plan_created_by(self):
        assert self.workout_plan.created_by == self.user

    def test_workout_plan_no_exercises(self):
        assert self.workout_plan.exercises.first() is None

    def test_workout_plan_exercises(self):
        self.workout_plan.exercises.add(self.exercise)
        assert self.workout_plan.exercises.first() == self.exercise

    def test_workout_plan_wrong_workout_type(self):
        self.workout_plan.workout_type = "EAR"
        print(self.workout_plan.workout_type)
        with pytest.raises(ValidationError) as e_info:
            self.workout_plan.save()
