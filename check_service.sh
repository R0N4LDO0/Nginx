#!/bin/bash

DATETIME=$(date '+%Y-%m-%d %H:%M:%S')
SERVICE="nginx"
STATUS=$(systemctl is-active $SERVICE)

if [ "$STATUS" = "active" ]; then
    echo "$DATETIME - $SERVICE - $STATUS - ONLINE" > ~/service_status/online.txt
else
    echo "$DATETIME - $SERVICE - $STATUS - OFFLINE" > ~/service_status/offline.txt
fi
