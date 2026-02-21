from embedded.interfaces.spi import SPIInterface

try:
    import spidev
except ImportError:
    spidev = None


class SPIReal(SPIInterface):
    def __init__(self, bus=0, device=0, max_speed_hz=1_000_000):
        if spidev is None:
            raise ImportError("spidev not installed")

        self.spi = spidev.SpiDev()
        self.bus = bus
        self.device = device
        self.max_speed_hz = max_speed_hz

        self.spi.open(bus, device)
        self.spi.max_speed_hz = max_speed_hz

    def transfer(self, tx: bytes) -> bytes:
        rx = self.spi.xfer2(list(tx))
        return bytes(rx)