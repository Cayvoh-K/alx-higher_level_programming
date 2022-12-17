#!/bin/bash
# script that sends a request to URL passed as an argument and displays only the status code of the response
curl "$1" -sw "%{http_code}" -o /dev/null
