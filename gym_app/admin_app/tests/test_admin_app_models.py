import pytest

from gym_app.admin_app.models import Exercise, WorkoutPlan
 


@pytest.mark.django_db
def test_workoutplan_add_exercise():
    pass
    
    # # Create Workout Plan
    # workoutplan_one = WorkoutPlan(name=None
    # )
    # print(workoutplan_one.name, workoutplan_one.workout_type)
    # workoutplan_one.save()


    # added_exercise = workoutplan_one.add_exercise(new_exercise)

    # assert added_exercise.name == new_exercise.name

    # Check for exercise attribute
    # Workout Plan Exercise to return number of exercises

@pytest.mark.django_db
def test_workoutplan_model():
    # Test Workout Plan Model 
    # Name is required
    # Workout is required

    # Create Model
    new_workoutplan = WorkoutPlan(
        workout_type="Chest"
    )

    # Save to database
    new_workoutplan.save()

    # Retrieved object from database
    retrieved_instance = WorkoutPlan.objects.get(name="")

    assert retrieved_instance.name == ""
    assert retrieved_instance.workout_type == "Chest"


    