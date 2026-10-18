from validators import normalize_url


def main():
    url = input("Enter a website URL: ").strip()
    normalized_url = normalize_url(url)
    
    print()
    print(20 * "-", "NORMALIZED URL", 20 * "-")
    print(normalized_url)
    print()


    
if __name__ == "__main__":
    main()