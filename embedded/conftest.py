import pytest

from embedded.backends.uart_mock import UARTMock
from embedded.backends.uart_real import UARTReal

from embedded.backends.i2c_mock import I2CMock
from embedded.backends.i2c_real import I2CReal

from embedded.backends.spi_mock import SPIMock
from embedded.backends.spi_real import SPIReal

from embedded.backends.gpio_mock import GPIOMock
from embedded.backends.gpio_real import GPIOReal


def pytest_addoption(parser):
    parser.addoption(
        "--hw",
        action="store_true",
        help="Run tests on real hardware"
    )


@pytest.fixture
def uart(request):
    if request.config.getoption("--hw"):
        uart = UARTReal()
    else:
        uart = UARTMock()

    uart.open()
    yield uart
    uart.close()


@pytest.fixture
def i2c(request):
    if request.config.getoption("--hw"):
        return I2CReal()
    return I2CMock()


@pytest.fixture
def spi(request):
    if request.config.getoption("--hw"):
        return SPIReal()
    return SPIMock()


@pytest.fixture
def gpio(request):
    if request.config.getoption("--hw"):
        return GPIOReal()
    return GPIOMock()