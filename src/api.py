
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.metals.dev/v1/latest"

params = {
    "currency": "USD",
    "unit": "toz"
}


def extract_with_api() -> float:
    """
    Retrieve the latest gold price using the Metals.Dev API.

    Returns
    -------
    float
        The latest gold price in USD per troy ounce.

    Raises
    ------
    ValueError
        If the API key is missing or the response contains invalid JSON.

    KeyError
        If the expected keys are missing from the API response.

    requests.exceptions.RequestException
        If the API request fails or the server returns an unsuccessful
        HTTP status code.
    """

    if not api_key:
        raise ValueError("API_KEY not found.")

    response = requests.get(
        url,
        params={**params, "api_key": api_key},
        timeout=10)
    response.raise_for_status()

    data = response.json()

    gold_price = float(data["metals"]["gold"])

    return gold_price
