import pytest

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

@pytest.mark.django_db
def test_work_remove_exercise(test_workout_plan, test_exercise):
    """
    Check exercise is removed from workout plan
    """

    # Add Exercise to workout plan
    test_workout_plan.add_exercise(test_exercise)

    # Verify Exercise is added to Workout Plan
    exercise = test_workout_plan.exercise_set.filter(name="test_exercise").first()
    assert exercise.name == "test_exercise"

    # Remove Exercise from Workput Plan
    test_workout_plan.remove_exercise(exercise)

    # Verify that exercise has been removed from workout plan
    assert test_workout_plan.exercise_set.filter(name="test_exercise").first() == None


@pytest.mark.django_db
def test_work_remove_non_existing_exercise(test_workout_plan, test_exercise):
    """
    Check exercise returns exercise is not in workout plan when trying to remove
    """

    # Try and remove exercise from work out plan
    test_workout_plan.remove_exercise(test_exercise)

    expected_mesage = "Exercise not in workout plan"
    
    assert expected_mesage == "Exercise not in workout plan"
