import serial

# Replace with your port, e.g., 'COM4' or '/tmp/ttyV1'
port = '/tmp/ttyV1'
baud = 9600

ser = serial.Serial(port, baud, timeout=1)
print(f"[Receiver] Listening on {port}")

try:
    while True:
        if ser.in_waiting:
            message = ser.readline().decode('utf-8').strip()
            if message:
                print(f"[Receiver] Received: {message}")
except KeyboardInterrupt:
    ser.close()
    print("\n[Receiver] Closed.")
