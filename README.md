# Gold & Currency Price Tracker

A Python project that retrieves gold price information using two different methods: extracting the displayed price from website HTML or retrieving gold price data through an external API.

## Features

- **URL Normalization:** Removes surrounding whitespace and adds `https://` when a URL does not include an HTTP or HTTPS scheme.
- **URL Validation:** Checks whether a URL uses HTTP or HTTPS and has a basic valid hostname format.
- **HTTP Requests:** Retrieves webpage content using the `requests` library.
- **API Integration:** Retrieves gold price information through the Metals.Dev API.
- **Environment Variables:** Uses `python-dotenv` to load sensitive configuration, such as API keys, from a `.env` file.
- **Error Handling:** Handles common HTTP request errors, timeouts, unsuccessful HTTP status codes, invalid JSON responses, and missing JSON keys.
- **HTML Parsing:** Parses webpage content using BeautifulSoup.
- **Gold Price Extraction:** Extracts the displayed gold price from parsed HTML or retrieves the gold price from an API response.
- **Command-Line Interface:** Allows users to choose between HTML-based extraction and API-based extraction.

## Technologies

- Python 3.10+
- [Requests](https://requests.readthedocs.io/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [Metals.Dev API](https://metals.dev/)
- Pytest (for testing)

## Project Structure

```text
Gold&Currency-Price-Tracker/
├── src/
│   ├── main.py
│   ├── api.py
│   ├── validators.py
│   ├── downloader.py
│   ├── parser.py
│   └── extractor.py
├── tests/
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- pip
- An API key from [Metals.Dev](https://metals.dev/) (required for API-based extraction)

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

## Configuration

API-based extraction requires an API key from [Metals.Dev](https://metals.dev/).

1. Create a `.env` file in the project root directory.
2. Add your API key:

   ```env
   API_KEY=your_api_key_here
   ```

3. The application uses `python-dotenv` to load the environment variable and `os.getenv()` to access the API key.

**Security:** Never commit your `.env` file or expose your API key in a public repository. The `.env` file is excluded from Git using `.gitignore`.

An optional `.env.example` file can be provided as a configuration template without including the actual API key:

```env
API_KEY=your_api_key_here
```

## Usage

Run the application from the project root:

```bash
python src/main.py
```

Choose one of the available extraction methods:

```text
1. Extract from HTML
2. Extract from API
Your choice:
```

### Method 1: Extract from HTML

Enter `1` to extract the gold price directly from a website.

When prompted, enter a website URL. For example:

```text
https://goldprice.com/
```

The application normalizes and validates the URL, sends an HTTP request, parses the returned HTML, and attempts to extract the displayed gold price.

Example output:

```text
-------------------- URL VALIDATION ----------------