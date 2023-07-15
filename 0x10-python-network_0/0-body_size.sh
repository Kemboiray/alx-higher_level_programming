#!/bin/bash
# Send a request to a url and display the size of the response body in bytes

curl -s "$1" | wc -c
