from datetime import datetime
import random
from time import sleep
import requests
import json


def generate_attribute_value(length=10):
    """
    returns a random attribute value with the given length in string format
    :param length: the length of the required attribute
    """
    lowercase_ascii_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    attribute_value = ''.join(random.choice(lowercase_ascii_letters) for _ in range(length))
    return attribute_value


def generate_insider_id():
    """
    gets the current timestamp that the function called and adds two zero as last characters
    """
    insider_id = str(datetime.now().timestamp() + 00)
    return insider_id


def wait_for_time(time: int):
    """
    waits for given duration
    :param time: seconds of the required wait duration, the format must be integer
    """
    sleep(time)


def send_post_request(endpoint, headers, json):
    """
    sends a post request to the given endpoint
    :param endpoint: the endpoint that will the post request sent
    :param headers: headers of the request
    :param json: payload of the request
    """
    return requests.post(endpoint, headers, json)


def get_response_body(response):
    """
    returns response body
    :param response: the response value that is set after sending the post request
    """
    return json.loads(response.content)
