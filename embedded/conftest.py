import pytest

from backends.uart_mock import UARTMock
from backends.uart_real import UARTReal

from backends.i2c_mock import I2CMock
from backends.i2c_real import I2CReal

from backends.spi_mock import SPIMock
from backends.spi_real import SPIReal

from backends.gpio_mock import GPIOMock
from backends.gpio_real import GPIOReal


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