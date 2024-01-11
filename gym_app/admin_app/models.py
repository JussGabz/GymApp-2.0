from django.db import models


# Create your models here.


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=50)
    workout_type = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def add_exercise(self, exercise):
        try:
            exercise.workoutplans.add(self)
        except Exception as e:
            raise e
        return exercise


class Exercise(models.Model):
    name = models.CharField(max_length=50, null=False)
    target_area = models.CharField(max_length=50)
    workoutplans = models.ManyToManyField(WorkoutPlan)
    date_added = models.DateTimeField(auto_now_add=True)

    
