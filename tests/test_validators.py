from validators import is_valid_url, normalize_url


def test_normalize_url():
    assert normalize_url("google.com") == "https://google.com"
    assert normalize_url("http://google.com") == "http://google.com"
    assert normalize_url("https://google.com") == "https://google.com"


def test_normalize_url_with_whitespace():
    assert normalize_url(" google.com ") == "https://google.com"


def test_is_valid_url():
    assert is_valid_url("https://google.com") is True
    assert is_valid_url("http://google.com") is True


def test_is_valid_url_invalid_scheme():
    assert is_valid_url("ftp://google.com") is False
    assert is_valid_url("file:///home/user/file.txt") is False


def test_is_valid_url_without_domain():
    assert is_valid_url("https://") is False
    assert is_valid_url("http://") is False
    assert is_valid_url("https:///path") is False


def test_is_valid_url_without_dot():
    assert is_valid_url("https://google") is False
    assert is_valid_url("http://github") is False


def test_is_valid_url_invalid_domain_dots():
    assert is_valid_url("https://.com") is False
    assert is_valid_url("https://google.com.") is False
    assert is_valid_url("https://google..com") is False
    assert is_valid_url("https://google...com") is False
    assert is_valid_url("https://..") is False
    assert is_valid_url("https://...") is False
