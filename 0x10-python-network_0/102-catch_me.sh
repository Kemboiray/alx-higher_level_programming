#!/bin/bash
# Prompt a specific response from the server
curl -s -o /dev/null -w "You find me!" 0.0.0.0:5000/catch_me
