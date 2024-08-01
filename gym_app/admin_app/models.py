from django.db import models
from django.contrib.auth.models import User
from .validators import validate_exercise_target_area, validate_workout_plan_workouttype
from .utils.exercise_utils import TARGET_AREA_CHOICES, WORKOUT_TYPE_CHOICES


class Exercise(models.Model):

    name = models.CharField(max_length=50, null=False, unique=True)
    target_area = models.CharField(
        max_length=50,
        choices=TARGET_AREA_CHOICES,
        validators=[validate_exercise_target_area],
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("readonly_exercises", "can view exercise but not add, change or delete.")
        ]

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return f"{self.id}: {self.name}"

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class WorkoutPlan(models.Model):

    # TODO - Add Date Updated Field for exercise
    name = models.CharField(max_length=50, null=False)
    workout_type = models.CharField(
        max_length=50,
        choices=WORKOUT_TYPE_CHOICES,
        validators=[validate_workout_plan_workouttype],
    )
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, related_name="exercises")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Workout Plan {self.id}: {self.name}"
