#!/usr/bin/python3
"""Print `id` of a GitHub user given its `username` and token"""

if __name__ == "__main__":
    import requests
    import sys

    username, token = sys.argv[1], sys.argv[2]
    url = f"https://api.github.com/user"
    auth = (username, token)
    res = requests.get(url, auth=auth)
    print(res.json().get("id"))
