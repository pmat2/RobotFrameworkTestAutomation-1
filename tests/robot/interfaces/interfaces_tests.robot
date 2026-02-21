*** Settings ***
Library    EmbeddedDriver.py  use_hw=${USE_HW}
Suite Teardown    Close

*** Variables ***
${USE_HW}    False

*** Test Cases ***

UART Mock Boot Test
    [Tags]    Embedded    UART
    Uart Write    BOOT
    ${resp}=    Uart Read    2.0
    Should Contain    ${resp}    READY

I2C Register Read Test
    [Tags]    Embedded    I2C
    ${val}=    I2c Read Register    0
    Should Be True    ${val} & 1

I2C Write And Read Back
    ${dummy}=    I2c Write Register    16    171
    ${val}=      I2c Read Register     16
    Should Be Equal As Integers    ${val}    171

SPI Known Pattern
    [Tags]    Embedded    SPI
    ${rx}=    Spi Transfer    AA
    Should Be Equal    ${rx}    55

GPIO Toggle Test
    [Tags]    Embedded    GPIO
    Gpio Set High    5
    ${val}=    Gpio Read    5
    Should Be Equal As Integers    ${val}    1
    Gpio Set Low    5
    ${val}=    Gpio Read    5
    Should Be Equal As Integers    ${val}    0