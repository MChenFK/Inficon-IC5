#!/bin/bash

# Create virtual serial ports using socat in the background
socat -d -d PTY,link=/tmp/ttyV0,raw,echo=0 PTY,link=/tmp/ttyV1,raw,echo=0 &
SOCAT_PID=$!
echo "Started socat with PID $SOCAT_PID"
sleep 2  # Wait a moment to ensure ports are ready

# Run receiver.py (listens on /tmp/ttyV1) in background
python3 receiver.py &
RECEIVER_PID=$!
echo "Started receiver.py with PID $RECEIVER_PID"
sleep 1  # Short delay to let receiver start

# Run sender.py (sends on /tmp/ttyV0)
python3 sender.py

# When sender.py exits (e.g., via Ctrl+C), kill the receiver and socat
echo "Killing receiver and socat processes..."
kill $RECEIVER_PID
kill $SOCAT_PID

# Remove the virtual ports (symlinks)
rm -f /tmp/ttyV0 /tmp/ttyV1

echo "Cleaned up and exiting."
