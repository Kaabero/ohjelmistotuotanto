*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set PasswordConfirmation  testi123
    Submit Credentials
    Registeration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set PasswordConfirmation  testi123
    Submit Credentials
    Registeration Should Fail With Message  Username should be at least 3 characters
    Register Page Should Be Open


Register With Valid Username And Too Short Password
    Set Username  validusername
    Set Password  test123
    Set PasswordConfirmation  test123
    Submit Credentials
    Registeration Should Fail With Message  Password should be at least 8 characters and it cannot consist of letters only
    Register Page Should Be Open

Register With Valid Username And Invalid Password
    Set Username  validusername
    Set Password  testitesti
    Set PasswordConfirmation  testitesti
    Submit Credentials
    Registeration Should Fail With Message  Password should be at least 8 characters and it cannot consist of letters only
    Register Page Should Be Open

Register With Nonmatching Password And Password Confirmation
    Set Username  validusername
    Set Password  testi123
    Set PasswordConfirmation  testi456
    Submit Credentials
    Registeration Should Fail With Message  Password and password confirmation differs
    Register Page Should Be Open

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  testi123
    Set PasswordConfirmation  testi123
    Submit Credentials
    Registeration Should Fail With Message  Username already taken
    Register Page Should Be Open

Login After Successful Registration
    Set Username  pirjo
    Set Password  pirjo123
    Set PasswordConfirmation  pirjo123
    Submit Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  pirjo
    Set Password  pirjo123
    Click Button  Login
    Main Page Should Be Open


Login After Failed Registration
    Set Username  pi
    Set Password  pirjo123
    Set PasswordConfirmation  pirjo123
    Submit Credentials
    Register Page Should Be Open
    Click Link  Login
    Login Page Should Be Open
    Set Username  pi
    Set Password  pirjo123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***

Registeration Should Succeed
    Welcome Page Should Be Open

Registeration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}


Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page