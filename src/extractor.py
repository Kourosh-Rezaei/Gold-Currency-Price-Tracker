from bs4 import BeautifulSoup


def extract_price(parsed_html: BeautifulSoup) -> str | None:
    """
    Extract the gold price from parsed HTML.

    Parameters
    ----------
    parsed_html : BeautifulSoup
        The parsed HTML content of the webpage.

    Returns
    -------
    str | None
        The gold price as a string if found, otherwise None.
    """
    
    price_tag = parsed_html.find("span", class_="hero")

    if price_tag:
        return price_tag.get_text(strip=True)

    return None