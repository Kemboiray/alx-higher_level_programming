#!/usr/bin/python3
"""Print HTTP errors"""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
