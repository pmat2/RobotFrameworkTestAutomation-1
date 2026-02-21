def test_read_status_register(i2c):
    status = i2c.read_register(0x00)
    assert status & 0x01


def test_write_and_read_register(i2c):
    i2c.write_register(0x10, 0xAB)
    assert i2c.read_register(0x10) == 0xAB