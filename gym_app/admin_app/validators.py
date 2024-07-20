from django.core.exceptions import ValidationError
from .utils.exercise_utils import TARGET_AREA_CHOICES


def validate_exercise_target_area(value):
    valid_target_area = [target_area for target_area, _ in TARGET_AREA_CHOICES]
    if value not in valid_target_area:
        raise ValidationError(f"{value} is not valid target area.")
