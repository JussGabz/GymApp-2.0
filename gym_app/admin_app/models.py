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

    def remove_exercise(self, exercise):

        # Check if exercise is apart of workout plan 
        exercise_exists = self.exercise_set.filter(name=exercise.name).first()
        # If apart of workout plan 

        if not exercise_exists:
            print("Exercise not in workout plan")
            return

        # Remove Exercise from Workoutplan
        try:
            self.exercise_set.remove(exercise)
            print("Exercise removed from Workout Plan")
        except Exception as e:
            raise e
        

class Exercise(models.Model):
    name = models.CharField(max_length=50, null=False)
    target_area = models.CharField(max_length=50)
    workoutplans = models.ManyToManyField(WorkoutPlan)
    date_added = models.DateTimeField(auto_now_add=True)

    
