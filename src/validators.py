from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    """
    Normalize a URL by trimming whitespace and adding https:// if needed.

    Parameters
    ----------
    url : str
        The URL to normalize.

    Returns
    -------
    str
        The normalized URL with whitespace removed and https://
        added if the URL does not start with http:// or https://.
    """

    url = url.strip()

    if not url.startswith(("https://", "http://")):
        url = f"https://{url}"

    return url


def is_valid_url(url: str) -> bool:
    """
    Check whether a URL has an accepted scheme and a valid basic domain format.

    Parameters
    ----------
    url : str
        The URL to validate.

    Returns
    -------
    bool
        True if the URL uses http or https and its hostname contains
        a dot without consecutive dots or a leading or trailing dot.
        False otherwise.
    """

    parsed_url = urlparse(url)
    domain = parsed_url.hostname

    if parsed_url.scheme not in ("http", "https"):
        return False

    if not domain or "." not in domain:
        return False

    return not (domain.startswith(".") or domain.endswith(".") or ".." in domain)
