import pytest

from gym_app.admin_app.models import Exercise

@pytest.mark.django_db
def test_exercise_model():

    exercise = Exercise(
        name="My Exercise",
        target_area="Chest"
    )

    assert exercise.name == "My Exercise"
    assert exercise.target_area =="Chest"


