import random
import string

class URLShortener:
    def _init_(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))

        while short_url in self.url_mapping:
            short_url = ''.join(random.choice(characters) for _ in range(6))

        self.url_mapping[short_url] = long_url
        return f"http://short.url/{short_url}"

    def resolve_url(self, short_url):
        short_code = short_url.split("/")[-1]
        long_url = self.url_mapping.get(short_code, None)

        if long_url:
            return long_url
        else:
            return "URL not found"

# Example Usage
shortener = URLShortener()

long_url = "https://www.example.com"
short_url = shortener.shorten_url(long_url)
print(f"Shortened URL: {short_url}")

resolved_url = shortener.resolve_url(short_url)
print(f"Resolved URL: {resolved_url}")