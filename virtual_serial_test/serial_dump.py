import time
import serial

#SERIAL_PORT = '/tmp/ttyV1'
SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
LOG_FILE = 'serial_log.txt'

SLEEP = 0

def main():
    try:
        with serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1) as ser, open(LOG_FILE, 'a') as log_file:
            print(f"Listening on {SERIAL_PORT} at {BAUDRATE} baud...")
            while True:
                line = ser.readline()
                if line:
                    decoded = line.decode('utf-8', errors='replace').strip()
                    #decoded = line.decode('ascii', errors='replace').strip()
                    print(decoded)
                    log_file.write(decoded + '\n')
                    log_file.flush()
                time.sleep(SLEEP)
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except KeyboardInterrupt:
        print("\nExiting on user interrupt.")

if __name__ == "__main__":
    main()
