import pytest
from rest_framework.test import APIClient
from django.utils import timezone, dateformat


@pytest.mark.django_db
@pytest.mark.parametrize("api_endpoint, request_data, expected_response", [
    ('/exercises/', {'name':'New Exercise', 'target_area': "Test_Area"}, {
        'id': 1,
        'name': 'New Exercise',
        'target_area': 'Test_Area',
    })
])
def test_exercise_api_create(create_api_object, api_endpoint, request_data, expected_response):
    """
    Test the creation of an object via API.

    This test function parameterizes different scenarios for creating objects via API.
    It uses the specified `api_call_function` to perform the API call and checks whether
    the response matches the expected response.

    Args:
        api_call_function (callable): A function that performs the API call.
        api_endpoint (str): The API endpoint to send the POST request.
        request_data (dict): The data to be sent in the POST request.
        expected_response (dict): The expected response after creating the object.

    Raises:
        AssertionError: If the response status code or data does not match the expected values.
    """

    # Get API Client()
    client = APIClient()

    expected_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
    response = create_api_object(client, api_endpoint, request_data)


    assert response.data['id'] == expected_response['id']
    assert response.data['name'] == expected_response['name']
    assert response.data['target_area'] == expected_response['target_area']
    assert 'date_added' in response.data
    assert response.data['date_added'] == expected_date

    assert response.status_code == 201


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
def test_exercise_api_put(test_exercise):
    """
        Update Exercise By ID -> PUT METHOD
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
        "date_added": dateformat.format(timezone.now(), 'Y-m-d H:i:s')
    }

@pytest.mark.django_db
def test_exercise_api_patch(test_exercise):
    """
        Update Exercise By ID - PATCH
    """

    test_exercise_id = test_exercise.id
    print(test_exercise.date_added)

    client = APIClient()

    response = client.patch(
        f'/exercises/{test_exercise_id}/',
        {
            "name": "Updated Exercise Name"
        },
        format='json'
    )
    assert response.status_code == 200
    assert response.data == {
        "id": test_exercise_id,
        "name": "Updated Exercise Name",
        "target_area": test_exercise.target_area,
        "date_added": dateformat.format(timezone.now(), 'Y-m-d H:i:s')
    }


