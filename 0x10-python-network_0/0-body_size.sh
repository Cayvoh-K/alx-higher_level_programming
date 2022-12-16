#!/bin/bash
# script that takes in a URL,sends request to taht URL and also displays the size of the body response
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
