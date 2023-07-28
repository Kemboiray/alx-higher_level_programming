#!/usr/bin/python3
"""
Display the value of the X-Request-Id variable found in the
header of an HTTP response
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
