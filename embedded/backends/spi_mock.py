from embedded.interfaces.spi import SPIInterface

class SPIMock(SPIInterface):
    def transfer(self, tx: bytes) -> bytes:
        if tx == b"\xAA":
            return b"\x55"
        return b"\x00"