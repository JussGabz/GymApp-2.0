from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Exercise(models.Model):
    # TODO - Add Date Updated Field for exercise
    name = models.CharField(max_length=50, null=False, unique=True)
    target_area = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"{self.id}: {self.name}"
    
    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class WorkoutPlan(models.Model):

    # TODO - Add Date Updated Field for exercise
    name = models.CharField(max_length=50, null=False)
    workout_type = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise, related_name='exercises')

    def __str__(self) -> str:
        return f"Workout Plan {self.id}: {self.name}"
