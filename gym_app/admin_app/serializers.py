from django.contrib.auth.models import Group, User
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

    exercises = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'workout_type', 'date_added', 'created_by', 'exercises']
    

    
