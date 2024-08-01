import pytest
from django.contrib.auth.models import User
from gym_app.admin_app.models import WorkoutPlan, Exercise
from gym_app.admin_app.serializers import WorkoutPlanSerializer
from datetime import datetime


@pytest.mark.django_db()
class TestWorkOutPlanSerializer:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.user = User.objects.create_user(username="Test User")
        self.workout_plan = WorkoutPlan.objects.create(
            name="Strength Workout", workout_type="STRENGTH", created_by=self.user
        )
        self.exercise = Exercise.objects.create(name="Bench Press", target_area="CHEST")
        self.workout_plan_serializer = WorkoutPlanSerializer

    def test_workplan_plan_serializer_data(self):
        workout_plan_serializer = self.workout_plan_serializer(self.workout_plan)

        assert workout_plan_serializer.data["id"] == self.workout_plan.id
        assert workout_plan_serializer.data["name"] == "Strength Workout"
        assert workout_plan_serializer.data["workout_type"] == "STRENGTH"
        assert workout_plan_serializer.data["date_added"] == datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        assert workout_plan_serializer.data["exercises"] == []
        assert workout_plan_serializer.data["created_by"] == "Test User"
