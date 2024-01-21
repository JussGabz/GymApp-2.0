import pytest
from rest_framework.test import APIClient
from django.utils import timezone, dateformat

@pytest.mark.django_db
def test_exercise_api_create():
    """
    Test Create an Exercise object via API 
    """

    """
    Exercise Request Example

    {   
        "name": "test_exercise",
        "workout_type: "Test Area"
    }
    
    ##########################################
    Exercise Response Example
    
    {
        'id': 1,
        'name': 'New Exercise',
        'target_area': 'Test_Area',
        'date_added': dateformat.format(timezone.now(), 'Y-m-d H:i:s'),
    }
    """
    client = APIClient()
    
    response = client.post('/exercises/', {
        'name':'New Exercise',
        'target_area': "Test_Area"
    }, format='json')

    assert response.status_code == 201
    assert response.data == {
        'id': 1,
        'name': 'New Exercise',
        'target_area': 'Test_Area',
        'date_added': dateformat.format(timezone.now(), 'Y-m-d H:i:s'),
    }

@pytest.mark.django_db
def test_exercise_api_delete(test_exercise):
    """
        Delete Exercise by ID
    """

    test_exercise_id = test_exercise.id

    client = APIClient()

    response = client.delete(
        f'/exercises/{test_exercise_id}/',
    )
    assert response.status_code == 204

@pytest.mark.django_db
def test_exercise_api_update(test_exercise):
    """
        Update Exercise By ID
    """

    test_exercise_id = test_exercise.id

    client = APIClient()

    response = client.put(
        f'/exercises/{test_exercise_id}/',
        {
            "name": "Updated Exercise Name",
            "target_area": "Test Target Area"
        },
        format='json'
    )
    assert response.status_code == 200
    assert response.data == {
        "id": test_exercise_id,
        "name": "Updated Exercise Name",
        "target_area": "Test Target Area",
        "date_added": "2024-01-01 00:00:00"
    }

