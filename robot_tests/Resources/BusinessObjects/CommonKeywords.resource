*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Begin Web Test
    Open browser    ${URL}     ${BROWSER}     service_log_path=${{os.path.devnull}}
    maximize browser window
    set selenium implicit wait    10s

End Web Test
    Close Browser