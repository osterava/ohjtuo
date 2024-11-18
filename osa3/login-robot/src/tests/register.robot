*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle1234
    Input New Command
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kallee  kalle1234
    Input New Command
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  as  kalle1234 
    Input New Command
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  as_*Ä":Ad;$@©∞|[]  kalle1234 
    Input New Command
    Output Should Contain  Username contains invalid characters

Register With Valid Username And Too Short Password
    Input Credentials  uudestaan  kale12
    Input New Command
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  uudestaan  kalleeeeee
    Input New Command
    Output Should Contain  Password must include numbers or special characters
*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kallee  kalle12345
