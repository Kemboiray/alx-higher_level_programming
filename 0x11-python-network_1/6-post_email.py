#!/usr/bin/python3
"""Send a POST request and display the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    res = requests.post(url, data)
    print(res.text)
