#!/bin/bash
# script that takes in URL,sends a POST request to the passed URL and displays the body of the response
curl "$1" -X POST -H "email=test@gmail.com&subject=I will always be here for PLD"
