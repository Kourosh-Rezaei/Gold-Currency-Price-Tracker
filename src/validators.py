def normalize_url(url: str) -> str:


    if not url.startswith(("https://", "http://")):
        url = f"https://{url}"

    return url

