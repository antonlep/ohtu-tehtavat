*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallo  kallo123kallo
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kallo123kallo
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kallo123kallo
    Output Should Contain  Username should be at least three characters long

Register With Valid Username And Too Short Password
    Input Credentials  sasqw  df5re
    Output Should Contain  Password should be at least eight characters long  

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sasqw  zxdsfersf
    Output Should Contain  Password should not contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
