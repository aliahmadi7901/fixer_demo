import requests
import json

from config import url


def get_rates():
    """
    send a get requests to the fixer.io api and get live rates
    :return: request.Response instance
    """
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None
