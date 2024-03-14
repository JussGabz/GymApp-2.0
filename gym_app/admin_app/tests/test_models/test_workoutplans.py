import pytest

@pytest.mark.django_db
def test_workoutplan_model(test_workout_plan):

    assert test_workout_plan.name == "test_workout_plan"
    assert test_workout_plan.workout_type =="test_type"