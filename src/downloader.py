import requests


def url_request(url: str) -> str:
    """
    Send a GET request to a URL and return the response text.

    Parameters
    ----------
    url : str
        The URL to send the request to.

    Returns
    -------
    str
        The text content of the HTTP response.

    Raises
    ------
    requests.exceptions.RequestException
        If the request fails or the server returns an unsuccessful
        HTTP status code.
    """

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.text
