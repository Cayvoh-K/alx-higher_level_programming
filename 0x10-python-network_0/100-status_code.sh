#!/bin/bash
# script that sends a request to URL passed as an argument and displays only the status code of the response
curl -sw "%{http_code}" "$1" -o /dev/null
