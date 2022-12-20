#!/usr/bin/python3
"""
- script that takes in a URL and an email
- sends a POST request to the passed URL
- takes an email as a parameter
- displays the body of the response
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as r:
        print(response.read() .decode("utf-8"))
