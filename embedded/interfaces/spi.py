class SPIInterface:
    def transfer(self, tx: bytes) -> bytes:
        raise NotImplementedError