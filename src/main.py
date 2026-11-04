import sys

import requests

from api import extract_with_api
from downloader import url_request
from extractor import extract_price
from parser import html_parser
from validators import is_valid_url, normalize_url


def main():
    print("1. Extract from HTML")
    print("2. Extract from API")

    choice = input("Your choice: ")

    if choice == "1":
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

    elif choice == "2":
        print()
        print(20 * "-", "API REQUEST", 20 * "-")

        try:
            price = extract_with_api()
            print("API request successful.")

        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            print(f"API request failed: {e}")
            sys.exit(1)

    else:
        print("Invalid choice.")
        sys.exit(1)

    if price is not None:
        print(f"Gold price: {price}")
    else:
        print("Gold price not found.")


if __name__ == "__main__":
    main()
