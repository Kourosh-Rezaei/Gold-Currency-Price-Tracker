import sys

import requests

from downloader import url_request
from extractor import extract_price
from parser import html_parser
from validators import is_valid_url, normalize_url


def main():
    url = input("Enter a website URL: ")
    normalized_url = normalize_url(url)

    print()
    print(20 * "-", "NORMALIZED URL", 20 * "-")
    print(normalized_url)
    print()

    print(20 * "-", "URL VALIDATION", 20 * "-")

    if is_valid_url(normalized_url):
        print("URL validation successful.")

    else:
        print("URL validation failed: Invalid URL.")
        sys.exit(1)

    
    print()
    print(20 * "-", "HTTP REQUEST", 20 * "-")

    try:
        html = url_request(normalized_url)
        print("HTTP request successful.")

    except requests.exceptions.RequestException as e:
        print(f"HTTP request failed: {e}")
        sys.exit(1)

    print()
    print(20 * "-", "HTML PARSING", 20 * "-")

    parsed_html = html_parser(html)
    print("HTML parsing successful.")

    print()
    print(20 * "-", "GOLD PRICE", 20 * "-")

    price = extract_price(parsed_html)

    if price:
        print(f"Gold price: {price}")
    else:
        print("Gold price not found.")


if __name__ == "__main__":
    main()
