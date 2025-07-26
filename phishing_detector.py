import tldextract
import validators

# Keywords often found in phishing URLs
phishing_keywords = ["verify", "login", "update", "free", "win", "urgent", "claim", "limited", "secure"]

def is_phishing(url):
    if not validators.url(url):
        return True  # Invalid URL = suspicious

    domain_parts = tldextract.extract(url)
    full_domain = f"{domain_parts.subdomain}.{domain_parts.domain}.{domain_parts.suffix}".lower()

    # Check suspicious keywords in URL and domain
    for word in phishing_keywords:
        if word in url.lower() or word in full_domain:
            return True

    # Check if it's in the known phishing list
    try:
        with open("sample_data/phishing_urls.txt", "r") as f:
            known_phish = f.read().splitlines()
        if url.strip() in known_phish:
            return True
    except:
        pass

    return False
