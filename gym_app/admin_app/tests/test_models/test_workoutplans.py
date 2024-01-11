import pytest

from gym_app.admin_app.models import WorkoutPlan, Exercise

@pytest.mark.django_db
def test_exercise_model():

    workoutplan = WorkoutPlan(
        name="My Workout",
        workout_type="Cardio"
    )

    assert workoutplan.name == "My Workout"
    assert workoutplan.workout_type =="Cardio"

@pytest.mark.django_db
def test_workplan_add_exercise():
    """
    Check Added exercise to Created Workout Plan
    """

    exercise = Exercise(
        name="My Exercise",
        target_area="My Target Area"
    )

    exercise.save()

    workoutplan = WorkoutPlan(
        name="My Workout Plan",
        workout_type="Cardio"
    )

    workoutplan.save()

    workoutplan.add_exercise(exercise)

    added_exercise = workoutplan.exercise_set.all()

    assert list(added_exercise) == [exercise]