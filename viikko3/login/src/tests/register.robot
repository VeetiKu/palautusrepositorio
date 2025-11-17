*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  kuveeti123
    Set Password  kuveeti123
    Set Passwordconfirmation  kuveeti123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ku
    Set Password  Ohtu123456
    Set Passwordconfirmation  Ohtu123456
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters long


Register With Valid Username And Too Short Password
    Set Username  ohtu123456
    Set Password  ku
    Set Passwordconfirmation  ku
    Click Button  Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  ohtu123456
    Set Password  kuveetiku
    Set Passwordconfirmation  kuveetiku
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  ohtu123456
    Set Password  kuveetikuku
    Set Passwordconfirmation  kuveetikukuk
    Click Button  Register
    Register Should Fail With Message  Password and confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Passwordconfirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Username already exists

*** Keywords ***
Set Username
    [Arguments]     ${username}
    Input Text      username  ${username}

Set Password
    [Arguments]     ${password}
    Input Text      password  ${password}

Set passwordconfirmation
    [Arguments]     ${password_confirmation}
    Input Text      password_confirmation  ${password_confirmation}

Register Should Fail With Message
    [Arguments]     ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go to Register Page

