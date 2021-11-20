*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  werty
    Set Password  qwer123qwer
    Set Password Again  qwer123qwer
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  we
    Set Password  qwer123qwer
    Set Password Again  qwer123qwer
    Submit Register Credentials
    Register Should Fail With Message  Username should be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  werty
    Set Password  qwer5
    Set Password Again  qwer5
    Submit Register Credentials
    Register Should Fail With Message  Password should be at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  werty
    Set Password  qwer5123
    Set Password Again  qwer5124
    Submit Register Credentials
    Register Should Fail With Message  Passwords don't match

Login After Succesful Registration
    Set Username  werty
    Set Password  qwer123qwer
    Set Password Again  qwer123qwer
    Submit Register Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  werty
    Set Password  qwer123qwer
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  we
    Set Password  qwer123qwer
    Set Password Again  qwer123qwer
    Submit Register Credentials
    Click Link  Login
    Login Page Should Be Open
    Set Username  wer
    Set Password  qwer123qwer
    Submit Credentials
    Login Should Fail WIth Message  Invalid username or password
