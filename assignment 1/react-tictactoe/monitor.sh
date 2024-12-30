#!/bin/bash

URL="http://localhost:5173"

STATUS_CODE=$(curl -o /dev/null -s -w "%{http_code}\n" $URL)

echo "$(date): HTTP Status Code: $STATUS_CODE" >> monitor.log

# 5173
