import pytest

from gym_app.admin_app.models import Exercise, WorkoutPlan

@pytest.mark.django_db
def test_workoutplan_display_exercises():
    
    new_exercise = Exercise(name="Bench Press", target_area="Chest")

    new_exercise.save()
    
    workoutplan_one = WorkoutPlan(
        name="Chest Workout Plan",
        workout_type="Chest Workout",
    )

    workoutplan_one.save()

    new_exercise.workoutplans.add(workoutplan_one)

    assert workoutplan_one.name == "Chest Workout Plan"

    # Check for exercise attribute
    # Workout Plan Exercise to return number of exercises

    