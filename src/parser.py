from bs4 import BeautifulSoup


def html_parser(html: str) -> BeautifulSoup:
    """
    Parse HTML content using BeautifulSoup.

    Parameters
    ----------
    html : str
        The raw HTML content of a webpage.

    Returns
    -------
    BeautifulSoup
        The parsed HTML content, ready for searching and extracting data.
    """

    return BeautifulSoup(html, "html.parser")