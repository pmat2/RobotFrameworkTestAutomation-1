def test_uart(uart):
    uart.write(b"BOOT\n")
    response = uart.read(timeout=2.0)

    assert b"READY" in response