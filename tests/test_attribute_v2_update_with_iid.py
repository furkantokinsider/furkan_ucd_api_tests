import json

import pytest
import requests
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
    wait_for_time(2)

    print("2. Verify that the API returns a 200 OK status code and '{}'.")
    assert response_attribute_v2_update.status_code == 200
    assert json.loads(response_attribute_v2_update.content) == {}

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
    wait_for_time(2)
    response_contact_api_payload_body = json.loads(response_contact_api_payload.content)
    assert response_contact_api_payload.status_code == 200
    assert response_contact_api_payload_body.attributes == {"su": attribute_value}

    print("4. Check that via Vertical API the newly created attribute exists in the system.")
    vertical_api_payload = {
        "partner": f"{test_partner}",
        "count_only": True,
        "sources": [
            "last"
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
    wait_for_time(2)
    vertical_api_response_body = json.loads(vertical_api_response.content)
    assert vertical_api_response.status_code == 200
    assert vertical_api_response_body["count"] == 1
