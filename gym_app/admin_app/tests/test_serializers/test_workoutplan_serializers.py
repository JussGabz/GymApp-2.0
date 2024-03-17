from django.test import TestCase
from gym_app.admin_app.models import Exercise, WorkoutPlan
from gym_app.admin_app.serializers import ExerciseSerializer, WorkoutPlanSerializer

class TestWorkOutPlanSerializer(TestCase):
    def setUp(self):
        # Create Sample Data for Workout Plan
        self.valid_data = {"name": "Test Work Out Plan", "workout_type": "Test Workout Type"}
        self.invalid_data = {"name": "Test Work Out Plan"}
        self.data_with_exercise = {"name": "Test Work Out Plan", "workout_type": "Test Workout Type", "exercises": ['d']}

    def test_valid_serializer_data(self):
        serializer = WorkoutPlanSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})
    
    def test_invalid_serializer_data(self):
        serializer = WorkoutPlanSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertTrue('workout_type' in serializer.errors)
    
    # Test Workout Serializer Saves JSON -> Python Object
    def test_valid_serializer_save(self):
        serializer = WorkoutPlanSerializer(data=self.valid_data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertIsInstance(instance, WorkoutPlan)

    # Test Workout Serializer Saves JSON w/ existing exercises
    def test_valid_serializer_with_exercise(self):
        serializer = WorkoutPlanSerializer(data=self.data_with_exercise)
        serializer.is_valid()
        instance = serializer.save()
        self.assertIsInstance(instance, WorkoutPlan)