from embedded.interfaces.i2c import I2CInterface


class I2CMock(I2CInterface):
    def __init__(self):
        self.registers = {
            0x00: 0x01,  # STATUS
            0x01: 0x00,  # ERROR
        }

    def read_register(self, addr: int) -> int:
        return self.registers.get(addr, 0xFF)

    def write_register(self, addr: int, value: int):
        self.registers[addr] = value