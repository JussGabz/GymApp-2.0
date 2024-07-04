from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan
from rest_framework import serializers
from gym_app.settings import DATETIME_FORMAT

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ExerciseSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT)
    
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'target_area', 'date_added']

class WorkoutPlanSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True)
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'workout_type', 'date_added', 'created_by', 'exercises']
    
    # Create Workout Plan with Exercises
    def create(self, validated_data):
        # Get Exercise Data
        print(validated_data)
        exercises_data = validated_data.pop('exercises')

        workout_plan = WorkoutPlan.objects.create(**validated_data)

        for exercise_data in exercises_data:
            exercise, created = Exercise.objects.get_or_create(**exercise_data)
            workout_plan.exercises.add(exercise)
        return workout_plan
    
    def update(self, instance, validated_data):
        # Get Validated Data from client
        exercise_data = validated_data.pop('exercises')
        print(exercise_data)

        # Get Data from instance
        # Replace Data in instance with client data
        # instance.exercises = validated_data.get('exercises')



    
