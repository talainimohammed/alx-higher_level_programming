#!/bin/bash
# Author: TALAINI Mohammed
curl -L -s -X HEAD -w "%{http_code}" "$1"
