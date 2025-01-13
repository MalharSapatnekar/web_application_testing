*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Begin Web Test
    Open Browser  http://www.amazon.com     headlessfirefox
    Maximize Browser Window

*** Keywords ***
Begin Web Test with Arg
    [Arguments]    ${arg1}
    Open Browser  http://www.amazon.com     ${arg1}
    Maximize Browser Window

End Web Test
    Close Browser