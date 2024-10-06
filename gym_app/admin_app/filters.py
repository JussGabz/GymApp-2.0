import django_filters
from .utils.exercise_utils import TARGET_AREA_CHOICES, WORKOUT_TYPE_CHOICES
from .models import Exercise, WorkoutPlan


class ExerciseFilter(django_filters.FilterSet):
    target_area = django_filters.ChoiceFilter(choices=TARGET_AREA_CHOICES)

    class Meta:
        model = Exercise
        fields = ("target_area",)


class WorkOutPlanFilter(django_filters.FilterSet):
    workout_type = django_filters.ChoiceFilter(choices=WORKOUT_TYPE_CHOICES)
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = WorkoutPlan
        fields = ("workout_type", "name")
