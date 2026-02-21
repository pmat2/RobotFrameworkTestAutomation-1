from embedded.interfaces.gpio import GPIOInterface
from pathlib import Path
import time


class GPIOReal(GPIOInterface):
    SYSFS_GPIO = Path("/sys/class/gpio")

    def _export(self, pin: int):
        gpio_path = self.SYSFS_GPIO / f"gpio{pin}"
        if not gpio_path.exists():
            (self.SYSFS_GPIO / "export").write_text(str(pin))
            time.sleep(0.1)

    def set_high(self, pin: int):
        self._export(pin)
        gpio = self.SYSFS_GPIO / f"gpio{pin}"
        (gpio / "direction").write_text("out")
        (gpio / "value").write_text("1")

    def set_low(self, pin: int):
        self._export(pin)
        gpio = self.SYSFS_GPIO / f"gpio{pin}"
        (gpio / "direction").write_text("out")
        (gpio / "value").write_text("0")

    def read(self, pin: int) -> int:
        self._export(pin)
        gpio = self.SYSFS_GPIO / f"gpio{pin}"
        (gpio / "direction").write_text("in")
        return int((gpio / "value").read_text().strip())