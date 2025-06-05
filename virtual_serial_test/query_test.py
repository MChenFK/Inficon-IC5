import serial
import time
import csv
from datetime import datetime

# Serial configuration
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

ACK = b'\x06'
NAK = b'\x15'

def send_query(cmd: str):
    ser.write((cmd + '\r').encode())  # Append carriage return
    response = ser.read_until(ACK).decode(errors='ignore').strip()
    if not response:
        print("No response.")
        return None
    elif response.endswith(chr(21)):  # NAK
        error_code = response[0]
        print(f"Error: Code '{error_code}' received")
        return None
    return response.rstrip(chr(6))  # Strip trailing ACK

# CSV setup
csv_filename = f"ic5_recorder_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(csv_filename, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Timestamp", "Recorder Output (raw)"])

    print("Polling QS 5 1... Press Ctrl+C to stop.")

    try:
        while True:
            timestamp = datetime.now().isoformat(timespec='seconds')
            recorder_output = send_query("QS 5 1")  # Recorder Output for Sensor 1

            print(f"{timestamp} | Recorder Output: {recorder_output}")
            writer.writerow([timestamp, recorder_output])
            csvfile.flush()

            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        ser.close()
