import string
import random

class UrlShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def shorten_url(self, original_url):
        short_code = self.generate_short_code()
        self.url_mapping[short_code] = original_url
        short_url = f"http://gfg.to/{short_code}"  # GeeksforGeeks short domain
        return short_url

    def expand_url(self, short_url):
        short_code = short_url.split("/")[-1]
        original_url = self.url_mapping.get(short_code, "URL not found")
        return original_url

# Example Usage
url_shortener = UrlShortener()

original_url = input("Enter the URL to shorten: ")
short_url = url_shortener.shorten_url(original_url)
print(f"Shortened URL: {short_url}")

expanded_url = url_shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")
