*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Page Loaded
    Page Should Contain Element  //h1[contains(text(),"Sign-In")]
    Element Text Should Be  //h1[contains(text(),"Sign-In")]  Sign-In
