import pytest
from rest_framework.test import APITestCase

from gym_app.admin_app.models import Exercise, WorkoutPlan
from django.contrib.auth.models import User
 
class WorkoutPlanViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="test_password")

    def create 

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

    default_user.save()

    new_workoutplan = WorkoutPlan(
        name="Push Ups",
        workout_type="Chest",
        created_by = default_user
    )

    # Save to database
    new_workoutplan.save()

    # assert

    # Retrieved object from database
    retrieved_instance = WorkoutPlan.objects.get(name="")

    assert retrieved_instance.name == ""
    assert retrieved_instance.workout_type == "Chest"


    