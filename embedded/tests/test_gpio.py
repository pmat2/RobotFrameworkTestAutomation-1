def test_gpio_set_high(gpio):
    gpio.set_high(5)
    assert gpio.read(5) == 1


def test_gpio_set_low(gpio):
    gpio.set_high(3)
    gpio.set_low(3)
    assert gpio.read(3) == 0