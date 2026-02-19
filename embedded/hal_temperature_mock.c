static int mock_temperature = 25;

void hal_set_mock_temperature(int temp) {
    mock_temperature = temp;
}

int hal_get_temperature(void) {
    return mock_temperature;
}
