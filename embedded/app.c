// app_test.c
#include <stdio.h>
#include <string.h>
#include "hal_temperature.h"

static int alarm_active;

void app_process(void) {
    alarm_active = hal_get_temperature() > 80;
}

int main(void) {
    char cmd[64];

    while (fgets(cmd, sizeof(cmd), stdin)) {
        if (sscanf(cmd, "SET_TEMP %d", &alarm_active)) {
            hal_set_mock_temperature(alarm_active);
            app_process();
            printf("OK\n");
        } else if (strncmp(cmd, "GET_ALARM", 9) == 0) {
            printf("ALARM=%d\n", alarm_active);
        }
        fflush(stdout);
    }
}
