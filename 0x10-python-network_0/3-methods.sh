#!/bin/bash
# uses curl to displays allowed methods from input url
curl -I "$1" 2>&1 | grep Allow | cut -d ' ' -f2-
