#!/bin/bash
# uses curl to return size of input URL
curl -I "$1" 2>&1 | grep Content-Length | cut -d ' ' -f2
