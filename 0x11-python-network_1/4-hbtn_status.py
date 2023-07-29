#!/usr/bin/python3
"""Fetch a url and display the body of the response"""

if __name__ == '__main__':
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    content = requests.get(url)
    print(f"Body response:\n\t- type: {type(content.text)}\
\n\t- content: {content.text}")
