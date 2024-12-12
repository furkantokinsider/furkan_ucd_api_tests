from utils.setup import *


@pytest.mark.health
def test_attribute_v2_invalid_payload():
    """
    Test case is: verify that a new attribute can be successfully created
        1. S1. Send a POST request to the /attribute/v2/update endpoint with an empty user object
        2. Verify that the API returns a 400 Bad Request status code.
        3. Check that the error message contains details about the validation failure.
    """
    empty_user_object_error_message = '{"error":"users cannot be empty: bad request"}\n'
    print("1. Send a POST request to the /attribute/v2/update endpoint with an empty user object")
    invalid_attribute_update_payload = {
        "partner": test_partner,
        "source": "web",
        "lane": 4,
        "users": [

        ]
    }
    response_invalid_attribute_v2_update = requests.post(UCD_ENDPOINT + ENDPOINTS.ATTRIBUTE_V2_UPDATE, headers=HEADERS,
                                                 json=invalid_attribute_update_payload)
    wait_for_time(10)
    print("Request is sent to '/attribute/v2/update' endpoint with an invalid payload!")

    print("2. Verify that the API returns a 400 Bad Request status code.")
    assert response_invalid_attribute_v2_update.status_code == 400
    print("API returned 400 Bad Request!")

    print("3. Check that the error message contains details about the validation failure.")
    assert response_invalid_attribute_v2_update.text == empty_user_object_error_message
    print("The error message received from API meets the expected error message!")
