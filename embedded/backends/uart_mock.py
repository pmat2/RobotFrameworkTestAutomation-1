from embedded.interfaces.uart import UARTInterface

class UARTMock(UARTInterface):
    def __init__(self):
        self.buffer = []

    def open(self):
        pass

    def close(self):
        pass

    def write(self, data: bytes):
        if data == b"BOOT\n":
            self.buffer.append(b"READY\n")

    def read(self, timeout: float) -> bytes:
        if self.buffer:
            return self.buffer.pop(0)
        return b""