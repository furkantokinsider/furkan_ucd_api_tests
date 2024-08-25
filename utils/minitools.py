import random
import string
from datetime import datetime
from random import *
from time import sleep


def generate_attribute_value(length=10):
    """
    returns a random attribute value with the given length in string format
    :param length: the length of the required attribute
    """
    attribute_value = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
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
