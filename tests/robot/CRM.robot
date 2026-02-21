*** Settings ***
Documentation    CRM site testing
Library          SeleniumLibrary  timeout=0:00:06

*** Variables ***
${BROWSER} =                       chrome
${URL} =                           https://automationplayground.com/crm/
${LOGIN} =                         admin@automationdemo.com
${PASSWORD} =                      pa55w0rd

*** Test Cases ***
Home page should load
    [Documentation]                Display home page
    [Tags]                         1001  Home  Smoke
    Open Browser                   ${URL}  ${BROWSER}
    Wait Until Page Contains       Customers Are Priority One!
    Close All Browsers

Login should succeed with valid credentials
    [Documentation]                Login with basic credentials
    [Tags]                         1002  Login  Smoke
    Login with valid credentials
    Close All Browsers

Login should fail with missing credentials
    [Documentation]                Login attempt with missing credentials
    [Tags]                         1003  Login  Functional
    Open Browser                   ${URL}  ${BROWSER}
    Click Link                     Sign In
    Log                            Leaving 'Email' and 'Password' fields empty
    Click Button                   Submit
    Page Should Contain Element    xpath=//h2[text()='Login']
    Close All Browsers

"Remember me" checkbox should persist email address
    [Documentation]                Login check with "Remember me" option
    [Tags]                         1004  Login  Functional
    Login with valid credentials  ${True}
    Click Link                     Sign Out
    Wait Until Page Contains       Signed Out
    Click Link                     Sign In
    Element Text Should Be         id=email-id  admin@automation.com
    Close All Browsers

Should be able to log out
    [Documentation]                Login and logout to confirm logout functionality
    [Tags]                         1005  Login  Functional
    Login with valid credentials
    Click Link                     Sign Out
    Wait Until Page Contains       Signed Out
    Close All Browsers

Customers page should display multiple customers
    [Documentation]                Login and confirm there are multiple entries in customers grid
    [Tags]                         1006  Contacts  Smoke
    Login with valid credentials
    ${ROW_COUNT} =  Get Element Count  xpath=//table[@id='customers']//tbody/tr
    Should Be True  ${ROW_COUNT} > 1
    Log                            ${ROW_COUNT} records present in customers grid
    Close All Browsers

Should be able to add new customer
    [Documentation]                Login and add new customer
    [Tags]                         1007  Contacts  Smoke
    Login with valid credentials
    Click Link                     New Customer
    Wait Until Page Contains       Add Customer
    Input Text                     EmailAddress  customer@automation.com
    Input Text                     FirstName  Customer #1
    Input Text                     LastName  Customer Last Name #1
    Input Text                     City  Honolulu
    Select From List By Value      id=StateOrRegion  HI
    Select Radio Button            gender  male
    Select Checkbox                name=promos-name
    Click Button                   Submit
    Wait Until Page Contains       Success! New customer added.
    Close All Browsers

Should be able to cancel adding new customer
    [Documentation]                Login go to add new customer form and click cancel
    [Tags]                         1008  Contacts  Functional
    Login with valid credentials
    Click Link                     New Customer
    Wait Until Page Contains       Add Customer
    Click Link                     Cancel
    Wait Until Page Contains       Our Happy Customers
    Close All Browsers

*** Keywords ***
Login with valid credentials
    [Arguments]    ${remember_me}=${False}
    [Documentation]                User logs in
    Open Browser                   ${URL}  ${BROWSER}
    Click Link                     Sign In
    Input Text                     id=email-id  ${LOGIN}
    Input Password                 id=password  ${PASSWORD}
    Run Keyword If  ${remember_me}  Select Checkbox  id=remember
    Click Button                   Submit
    Wait Until Page Contains       Our Happy Customers
