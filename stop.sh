#!/bin/bash
if [ -f pid.txt ]; then
    while read -r pid; do
        kill $pid
    done <pid.txt
    rm pid.txt
    echo "PID file destroyed"
else
    echo "No pid file trying 2"
fi
./kill_port 5000
./kill_port 5001
./kill_port 5002