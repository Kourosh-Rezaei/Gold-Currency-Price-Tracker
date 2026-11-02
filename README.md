# Gold & Currency Price Tracker

A Python project that retrieves gold price information from a website by sending HTTP requests, parsing HTML content, and extracting the displayed gold price.

## Features

- **URL Normalization:** Removes surrounding whitespace and adds `https://` when a URL does not include an HTTP or HTTPS scheme.
- **URL Validation:** Checks whether a URL uses HTTP or HTTPS and has a basic valid hostname format.
- **HTTP Requests:** Retrieves webpage content using the `requests` library.
- **Error Handling:** Handles common HTTP request errors, including connection failures, timeouts, and unsuccessful HTTP status codes.
- **HTML Parsing:** Parses webpage content using BeautifulSoup.
- **Gold Price Extraction:** Extracts the displayed gold price from the parsed HTML.
- **Command-Line Interface:** Prompts the user for a website URL and displays the processing status and extracted price.

## Technologies

- Python 3.10+
- [Requests](https://requests.readthedocs.io/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Pytest (for testing)

## Project Structure

```text
Gold&Currency-Price-Tracker/
├── src/
│   ├── main.py
│   ├── validators.py
│   ├── downloader.py
│   ├── parser.py
│   └── extractor.py
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.10 or newer
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd Gold&Currency-Price-Tracker
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

Run the application from the project root:

```bash
python src/main.py
```

When prompted, enter a website URL. For example:

```text
https://goldprice.com/
```

The application normalizes and validates the URL, sends an HTTP request, parses the returned HTML, and attempts to extract the gold price.

Example output:

```text
-------------------- URL VALIDATION --------------------
URL validation successful.

-------------------- HTTP REQUEST --------------------
HTTP request successful.

-------------------- HTML PARSING --------------------
HTML parsing successful.

-------------------- GOLD PRICE --------------------
Gold price: $3,875.65
```

*The displayed price is an example. Actual prices and output may vary depending on the website response and current market conditions.*

## Testing

Run the test suite from the project root:

```bash
python -m pytest tests -v
```

Tests can be added for URL validation, URL normalization, HTTP request handling, HTML parsing, and gold price extraction.

## Error Handling

The application may report an error when:

- The URL is invalid.
- The website cannot be reached.
- The request times out.
- The server returns an unsuccessful HTTP status code.
- The expected gold price element cannot be found in the HTML.

Website structure changes may affect price extraction. The application depends on the HTML returned by the selected website.

## Data Source

The current target website is [GoldPrice.com](https://goldprice.com/).

The extracted price is the value displayed by the website, not a guaranteed executable market quote. Availability and accuracy depend on the source website.

## License

No license has been specified yet.