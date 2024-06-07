*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Search Completed
    Wait Until Page Contains  results for "${PRODUCT}"

Click Product Link
    [Documentation]  Clicks on the first product in the search results list
    Click Element    xpath=//div[@data-index="1"]//img[@class="s-image"]