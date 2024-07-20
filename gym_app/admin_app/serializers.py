from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan
from rest_framework import serializers
from gym_app.settings import DATETIME_FORMAT


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class ExerciseSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT)

    class Meta:
        model = Exercise
        fields = ["id", "name", "target_area", "date_added"]


class WorkoutPlanSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True, read_only=True)
    exercise_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Exercise.objects.all(), write_only=True
    )
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = WorkoutPlan
        fields = [
            "id",
            "name",
            "workout_type",
            "date_added",
            "created_by",
            "exercises",
            "exercise_ids",
        ]

    def create(self, validated_data):

        # Extract Exercise IDs from request
        exercise_ids = validated_data.pop("exercise_ids")
        workout_plan = WorkoutPlan.objects.create(**validated_data)
        workout_plan.exercises.set(exercise_ids)
        return workout_plan

    def update(self, instance, validated_data):
        # Get Validated Data from client
        exercise_ids = validated_data.pop("exercise_ids", None)

        if exercise_ids is not None:
            instance.exercises.set(exercise_ids)

        return super().update(instance, validated_data)
