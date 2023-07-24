#!/usr/bin/python3
"""Fetch a url and display the body of the response"""

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as page:
    content = page.read()

print(f"Body response:\n\t- type: {type(content)}\n\t- content: {content}\n\t\
- utf8 content: {content.decode()}")
