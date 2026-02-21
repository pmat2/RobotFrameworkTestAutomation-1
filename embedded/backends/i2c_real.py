from embedded.interfaces.i2c import I2CInterface

try:
    from smbus2 import SMBus
except ImportError:
    SMBus = None


class I2CReal(I2CInterface):
    def __init__(self, bus_id=1, device_addr=0x20):
        if SMBus is None:
            raise ImportError("smbus2 not installed")

        self.bus_id = bus_id
        self.device_addr = device_addr
        self.bus = SMBus(bus_id)

    def read_register(self, addr: int) -> int:
        return self.bus.read_byte_data(self.device_addr, addr)

    def write_register(self, addr: int, value: int):
        self.bus.write_byte_data(self.device_addr, addr, value)