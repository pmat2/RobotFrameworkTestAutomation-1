*** Settings ***
Library    EmbeddedDriver.py  use_hw=${USE_HW}
Suite Teardown    Close

*** Variables ***
${USE_HW}    False

*** Test Cases ***

UART Mock Boot Test
    [Documentation]                 UART read command BOOT
    [Tags]                          3001            Embedded            UART
    Uart Write                      BOOT
    ${resp}=                        Uart Read    2.0
    Should Contain                  ${resp}    READY

I2C Register Read Test
    [Documentation]                 I2C read reguster 0
    [Tags]                          3002            Embedded            I2C
    ${val}=                         I2c Read Register    0
    Should Be True                  ${val} & 1

I2C Write And Read Back
    [Documentation]                 I2C write value to address, read address
    [Tags]                          3003            Embedded            I2C
    ${dummy}=                       I2c Write Register    16    171
    ${val}=                         I2c Read Register     16
    Should Be Equal As Integers     ${val}    171

SPI Known Pattern
    [Documentation]                SPI transfer
    [Tags]                         3004            Embedded            SPI
    ${rx}=                         Spi Transfer     AA
    Should Be Equal                ${rx}    55

GPIO Toggle Test
    [Documentation]                GPIO Set High, Set Low, Read tests
    [Tags]                         3005            Embedded            GPIO
    Gpio Set High                  5
    ${val}=                        Gpio Read    5
    Should Be Equal As Integers    ${val}    1
    Gpio Set Low                   5
    ${val}=    Gpio Read           5
    Should Be Equal As Integers    ${val}    0