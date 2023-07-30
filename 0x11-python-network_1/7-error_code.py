#!/usr/bin/python3
"""Print HTTP errors"""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    if res.ok:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")
