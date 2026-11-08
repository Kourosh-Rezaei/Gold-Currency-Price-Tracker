
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.metals.dev/v1/latest"



def extract_with_api(metal: str, currency: str, unit: str) -> float:
    """
    Retrieve the latest metal price using the Metals.dev API.

    Parameters
    ----------
    metal : str
        The metal name (gold, silver, platinum, or palladium).
    currency : str
        The desired currency (e.g., USD, EUR, GBP).
    unit : str
        The desired unit (e.g., toz, g, kg).

    Returns
    -------
    float
        The latest metal price.

    Raises
    ------
    ValueError
        If the API key is missing.
    KeyError
        If the expected keys are missing from the API response.
    requests.exceptions.RequestException
        If the API request fails.
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


