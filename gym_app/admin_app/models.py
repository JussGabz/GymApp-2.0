from django.db import models


# Create your models here.


class Exercise(models.Model):
    # TODO - Add Date Updated Field for exercise
    name = models.CharField(max_length=50, null=False)
    target_area = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)


class WorkoutPlan(models.Model):

    # TODO - Add Date Updated Field for exercise
    name = models.CharField(max_length=50)
    workout_type = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise)



    
