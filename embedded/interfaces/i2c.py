class I2CInterface:
    def read_register(self, addr: int) -> int:
        raise NotImplementedError

    def write_register(self, addr: int, value: int):
        raise NotImplementedError