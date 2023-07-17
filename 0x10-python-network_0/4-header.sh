#!/bin/bash
# Send a GET request with a header variable-value pair
curl -sH "X-School-User-Id: 98" "$1"
