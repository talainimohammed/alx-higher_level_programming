#!/bin/bash
# Bash script that takes in a URL, sends a request
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
