from django.contrib.auth.models import User
from .models import Exercise, WorkoutPlan
from rest_framework import serializers
from gym_app.settings import DATETIME_FORMAT
from .utils.exercise_utils import TARGET_AREA_CHOICES, WORKOUT_TYPE_CHOICES


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ExerciseSerializer(serializers.ModelSerializer):
    date_added = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT)

    class Meta:
        model = Exercise
        fields = ["id", "name", "target_area", "date_added"]

class WorkoutTypeChoicesSerializer(serializers.Serializer):
    workout_type = serializers.ChoiceField(choices=WORKOUT_TYPE_CHOICES)

class WorkoutPlanSerializer(serializers.ModelSerializer):

    exercises = ExerciseSerializer(many=True, read_only=True)
    exercise_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Exercise.objects.all(), write_only=True
    )
    created_by = serializers.StringRelatedField(read_only=True)
    date_added = serializers.DateTimeField(read_only=True, format=DATETIME_FORMAT)
    workout_type = serializers.SerializerMethodField()

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

    def get_workout_type(self, obj):
        return obj.get_workout_type_display()
