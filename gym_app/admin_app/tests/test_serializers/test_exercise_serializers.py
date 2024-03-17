from django.test import TestCase
from gym_app.admin_app.models import Exercise, WorkoutPlan
from gym_app.admin_app.serializers import ExerciseSerializer, WorkoutPlanSerializer

class TestExerciseSerializer(TestCase):
    def setUp(self):
        # Create sample data for test
        self.valid_data = {"name": "Test Exercise", "target_area":"Test Area"}
        self.invalid_data = {"name": "Test Exercise"}

    def test_valid_serializer_data(self):
        serializer = ExerciseSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {}) # No Errors Expected
    
    def test_invalid_serializer_data(self):
        serializer = ExerciseSerializer(data=self.invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertTrue('target_area' in serializer.errors)
    
    def test_valid_serializer_save(self):
        serializer = ExerciseSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        instance = serializer.save()
        self.assertIsInstance(instance, Exercise)

