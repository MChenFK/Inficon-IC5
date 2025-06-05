import serial
import time

# Replace with your port, e.g., 'COM3' or '/tmp/ttyV0'
port = '/tmp/ttyV0'
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
print(f"[Sender] Writing to {port}")

try:
    while True:
        message = f"Hello at {time.ctime()}\n"
        ser.write(message.encode('utf-8'))
        print(f"[Sender] Sent: {message.strip()}")
        time.sleep(2)
except KeyboardInterrupt:
    ser.close()
    print("\n[Sender] Closed.")
