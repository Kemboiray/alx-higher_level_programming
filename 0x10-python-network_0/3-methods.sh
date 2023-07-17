#!/bin/bash
# Display all HTTP methods a server accepts
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
