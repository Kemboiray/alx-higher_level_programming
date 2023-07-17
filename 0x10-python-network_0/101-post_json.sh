#!/bin/bash
# Send a POST request using a JSON file
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
