from urllib.parse import urlparse

def extract_features(url):

    url_length = len(url)

    ip_address = 1 if any(char.isdigit() for char in urlparse(url).netloc) else 0

    ssl_state = 1 if url.startswith("https") else 0

    age_domain = 1
    google_index = 1

    features = [
        ip_address,
        url_length,
        0, 0, 0, 0, 0,
        ssl_state,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        age_domain,
        0, 0, 0,
        google_index,
        0, 0
    ]

    analysis = {
        "url_length": url_length,
        "ip_address": ip_address,
        "ssl_state": ssl_state
    }

    return features, analysis