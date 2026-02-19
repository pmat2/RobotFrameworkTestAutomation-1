*** Settings ***
Library    app_driver.py

*** Test Cases ***
Alarm Off Below Threshold
    Start
    ${RESULT}=    Send    SET_TEMP 40
    Should Be Equal    ${RESULT}    OK
    ${RESULT}=    Send    GET_ALARM
    Should Be Equal    ${RESULT}    ALARM=0
    Stop

Alarm On Above Threshold
    Start
    ${r}=    Send    SET_TEMP 85
    Should Be Equal    ${r}    OK
    ${r}=    Send    GET_ALARM
    Should Be Equal    ${r}    ALARM=1
    Stop
