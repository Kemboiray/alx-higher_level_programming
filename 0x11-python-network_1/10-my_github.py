#!/usr/bin/python3
"""Print `id` of a GitHub user given its `username` and token"""

if __name__ == "__main__":
    import requests
    import sys

    username, token = sys.argv[1], sys.argv[1:][0] or "token"
    url = f"https://api.github.com/users/{username}"
    data = {"Authorization": f"Bearer {token}"}
    res = requests.get(url, data)
    print(res.json()["id"])
