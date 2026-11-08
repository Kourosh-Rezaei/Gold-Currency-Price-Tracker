
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.metals.dev/v1/latest"



def extract_with_api(metal: str, currency: str, unit: str) -> float:
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

    params = {
        "api_key": api_key,
        "currency": currency,
        "unit": unit,
        }

    response = requests.get(
        url,
        params= params,
        timeout=10
        )
    
    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        raise ValueError(f"API returns an unseccessful response: {data}")

    price = float(data["metals"][metal])

    return price


