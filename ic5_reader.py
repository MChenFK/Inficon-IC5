import serial
from .parser import parse_ic5_output
from .config import DEFAULT_PORT, DEFAULT_BAUDRATE

class IC5Reader:
    def __init__(self, port=DEFAULT_PORT, baudrate=DEFAULT_BAUDRATE, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def read_line(self):
        """Reads one line of data from the IC5 and parses it."""
        if self.ser.in_waiting > 0:
            raw = self.ser.readline().decode('utf-8', errors='ignore').strip()
            return parse_ic5_output(raw)
        return None

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
