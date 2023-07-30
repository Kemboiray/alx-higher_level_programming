#!/usr/bin/python3
"""Send a POST request and display the body of the response"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        param = sys.argv[1]
    else:
        param = ""
    data = {'q': param}
    res = requests.post(url, data)
    try:
        d = res.json()
    except Exception as e:
        print(e)
        # print("Not a valid JSON")
    else:
        if d:
            print(f"[{d['id']}] {d['name']}")
        else:
            print("No result")
