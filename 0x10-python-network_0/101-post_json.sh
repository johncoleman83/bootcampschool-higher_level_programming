#!/bin/bash
# POST request from json file w/ curl & --data params to input URL
curl -sX POST "$1" -d "@$2" --header "Content-Type: application/json"
