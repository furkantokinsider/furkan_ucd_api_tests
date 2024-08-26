from utils.setup import *


@pytest.mark.health
def test_attribute_v2_update_with_iid():
    """
    Test case is: verify that a new attribute can be successfully created
        1. Send a POST request to the '/attribute/v2/update' endpoint with valid attribute data.
        2. Verify that the API returns a 200 OK status code and '{}'.
        3. Check that via Contact the newly created attribute exists in the system.
        4. Check that via Vertical API the newly created attribute exists in the system.
    """

    print("1. Send a POST request to the '/attribute/v2/update' endpoint with valid attribute data.")
    insider_id = generate_insider_id()
    attribute_value = generate_attribute_value()
    valid_attribute_update_payload = {
        "partner": test_partner,
        "source": "web",
        "lane": 4,
        "users": [
            {
                "insider_id": insider_id,
                "attributes": {
                    "su": attribute_value
                }
            }
        ]
    }
    response_attribute_v2_update = requests.post(UCD_ENDPOINT + ENDPOINTS.ATTRIBUTE_V2_UPDATE, headers=HEADERS,
                                                     json=valid_attribute_update_payload)
    wait_for_time(10)
    print("Request is successfully sent to '/attribute/v2/update' endpoint with valid attribute data!")

    print("2. Verify that the API returns a 200 OK status code and '{}'.")
    assert response_attribute_v2_update.status_code == 200
    assert get_response_body(response_attribute_v2_update) == {}
    print("API returned 200 OK and the body content is equal to '{}'!")

    print("3. Check that via Contact the newly created attribute exists in the system")
    contact_api_payload = {
        "partner": test_partner,
        "sources": [
            "web"
        ],
        "insider_id": insider_id,
        "attributes": [
            "su"
        ]
    }
    response_contact_api_payload = requests.post(UCD_ENDPOINT + ENDPOINTS.CONTACT_API, headers=HEADERS,
                                                     json=contact_api_payload)
    wait_for_time(10)
    response_contact_api_payload_body = get_response_body(response_contact_api_payload)
    assert response_contact_api_payload.status_code == 200
    assert response_contact_api_payload_body["attributes"] == {"su": attribute_value}
    print("Contact API request status code is 200 and attribute object has the necessary value!")

    print("4. Check that via Vertical API the newly created attribute exists in the system.")
    vertical_api_payload = {
        "partner": test_partner,
        "count_only": True,
        "sources": [
            "web"
        ],
        "columns": [
            "iid"
        ],
        "main_group": {
            "filter_groups": [
                {
                    "attr_filters": [
                        {
                            "attrs": [
                                {
                                    "key": "su",
                                    "operator": "eq",
                                    "values": [
                                        attribute_value
                                    ]
                                },
                                {
                                    "key": "iid",
                                    "operator": "eq",
                                    "values": [
                                        insider_id
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
    vertical_api_response = requests.post(UCD_ENDPOINT + ENDPOINTS.VERTICAL_API, headers=HEADERS,
                                              json=vertical_api_payload)
    wait_for_time(10)
    vertical_api_response_body = get_response_body(vertical_api_response)
    assert vertical_api_response.status_code == 200
    assert vertical_api_response_body["count"] == 1
    print("Vertical API endpoint status code is 200 and count returns '1' as expected!")
