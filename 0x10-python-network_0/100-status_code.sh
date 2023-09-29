#!/bin/bash
# Author: TALAINI Mohammed
# Bash script that sends a
# request to a URL passed as
# an argument, and displays
# only the status code of the response.
curl -L -s -X HEAD -w "%{http_code}" "$1"
