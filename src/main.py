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
        print("Valid URL")

    else:
        print("Invalid URL")

if __name__ == "__main__":
    main()
