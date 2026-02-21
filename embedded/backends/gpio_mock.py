from embedded.interfaces.gpio import GPIOInterface

class GPIOMock(GPIOInterface):
    def __init__(self):
        self.pins = {}

    def set_high(self, pin: int):
        self.pins[pin] = 1

    def set_low(self, pin: int):
        self.pins[pin] = 0

    def read(self, pin: int) -> int:
        return self.pins.get(pin, 0)