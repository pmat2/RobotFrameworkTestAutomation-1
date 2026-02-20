*** Settings ***
Library    AppDriver.py

*** Test Cases ***
Alarm Off Below Threshold
    [Documentation]                 Set temperature below threshold and get alarm result, expect alarm off
    [Tags]                          2001          Embedded      Smoke
    Start
    ${RESULT}=                      Send          SET_TEMP 40
    Should Be Equal                 ${RESULT}     OK
    ${RESULT}=                      Send          GET_ALARM
    Should Be Equal                 ${RESULT}     ALARM=0
    Stop

Alarm On Above Threshold
    [Documentation]                 Set temperature above threshold and get alarm result, expect alarm on
    [Tags]                          2002          Embedded      Smoke
    Start
    ${RESULT}=                      Send          SET_TEMP 85
    Should Be Equal                 ${RESULT}     OK
    ${RESULT}=                      Send          GET_ALARM
    Should Be Equal                 ${RESULT}     ALARM=1
    Stop
