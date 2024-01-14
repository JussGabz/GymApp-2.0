import pytest

from gym_app.admin_app.models import WorkoutPlan, Exercise

@pytest.mark.django_db
def test_workoutplan_model(test_workout_plan):

    assert test_workout_plan.name == "test_workout_plan"
    assert test_workout_plan.workout_type =="test_type"

@pytest.mark.django_db
def test_workplan_add_exercise(test_exercise, test_workout_plan):
    """
    Check Added exercise to Created Workout Plan
    """
    
    # Add exercise to workout plan
    test_workout_plan.add_exercise(test_exercise)

    # TODO - Query by WorkOut ID
    # Query workout plan exercise by name
    added_exercise = test_workout_plan.exercise_set.filter(name="test_exercise").first()
    assert added_exercise == test_exercise