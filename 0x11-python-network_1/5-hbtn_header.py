#!/usr/bin/python3
"""
Display the value of the X-Request-Id variable found in the
header of an HTTP response
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers['X-Request-Id'])
