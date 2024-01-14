import pytest

@pytest.mark.django_db
def test_exercise_model(test_exercise):

    assert test_exercise.name == "test_exercise"
    assert test_exercise.target_area =="test_target_area"


