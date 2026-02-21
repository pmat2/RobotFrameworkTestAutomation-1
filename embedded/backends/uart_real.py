import serial
from embedded.interfaces.uart import UARTInterface


class UARTReal(UARTInterface):
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200, timeout=1.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def open(self):
        self.ser = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=self.timeout
        )

    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()

    def write(self, data: bytes):
        if not self.ser:
            raise RuntimeError("UART not opened")
        self.ser.write(data)

    def read(self, timeout: float) -> bytes:
        if not self.ser:
            raise RuntimeError("UART not opened")
        self.ser.timeout = timeout
        return self.ser.readline()