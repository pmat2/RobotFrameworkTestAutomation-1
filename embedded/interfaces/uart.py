class UARTInterface:
    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def write(self, data: bytes):
        raise NotImplementedError

    def read(self, timeout: float) -> bytes:
        raise NotImplementedError