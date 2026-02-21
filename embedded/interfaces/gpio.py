class GPIOInterface:
    def set_high(self, pin: int):
        raise NotImplementedError

    def set_low(self, pin: int):
        raise NotImplementedError

    def read(self, pin: int) -> int:
        raise NotImplementedError