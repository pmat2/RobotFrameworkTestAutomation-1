from embedded.backends.uart_mock import UARTMock
from embedded.backends.uart_real import UARTReal

from embedded.backends.i2c_mock import I2CMock
from embedded.backends.i2c_real import I2CReal

from embedded.backends.spi_mock import SPIMock
from embedded.backends.spi_real import SPIReal

from embedded.backends.gpio_mock import GPIOMock
from embedded.backends.gpio_real import GPIOReal


class EmbeddedDriver:
    ROBOT_LIBRARY_SCOPE = "SUITE"

    def __init__(self, use_hw=False):
        self.use_hw = use_hw

        self.uart = UARTReal() if use_hw else UARTMock()
        self.i2c = I2CReal() if use_hw else I2CMock()
        self.spi = SPIReal() if use_hw else SPIMock()
        self.gpio = GPIOReal() if use_hw else GPIOMock()

        self.uart.open()

    # ===== UART =====
    def uart_write(self, data: str):
        self.uart.write(data.encode())

    def uart_read(self, timeout=2.0):
        return self.uart.read(timeout).decode(errors="ignore")

    # ===== I2C =====
    def i2c_read_register(self, addr: int):
        return self.i2c.read_register(addr)

    def i2c_write_register(self, addr: int, value: int):
        self.i2c.write_register(addr, value)

    # ===== SPI =====
    def spi_transfer(self, hex_data: str):
        tx = bytes.fromhex(hex_data)
        rx = self.spi.transfer(tx)
        return rx.hex().upper()

    # ===== GPIO =====
    def gpio_set_high(self, pin: int):
        self.gpio.set_high(pin)

    def gpio_set_low(self, pin: int):
        self.gpio.set_low(pin)

    def gpio_read(self, pin: int):
        return self.gpio.read(pin)

    def close(self):
        self.uart.close()