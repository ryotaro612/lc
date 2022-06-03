import hashlib
class Codec:
    
    def __init__(self):
        self.cache = dict()
        self.prefix = 'http://tinyurl.com/'
    """
    http://tinyurl.com/
    [0-9,a-z,A-Z].length = 10+26*2 = 52+10 = 62
    n -> 62^n > 252000 if n = 3
    """
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        suffix = hashlib.sha256(longUrl.encode()).hexdigest()[:3]
        self.cache[suffix] = longUrl
        return f"{self.prefix}{suffix}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """       
        return self.cache[shortUrl[len(self.prefix):]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
