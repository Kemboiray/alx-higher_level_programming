#!/usr/bin/python3
"""Print last 10 commits on a repo given the repo name and owner"""

if __name__ == "__main__":
    import requests
    import sys

    repo, owner = sys.argv[1], sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    res = requests.get(url)
    json = res.json()
    for i in range(0, 10):
        if i < len(json):
            print(f"{json[i].get('sha')}:\
 {json[i].get('commit').get('author').get('name')}")
