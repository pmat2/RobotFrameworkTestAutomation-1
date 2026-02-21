def test_spi_known_pattern(spi):
    rx = spi.transfer(b"\xAA")
    assert rx == b"\x55"


def test_spi_unknown_pattern(spi):
    rx = spi.transfer(b"\xFF")
    assert rx == b"\x00"