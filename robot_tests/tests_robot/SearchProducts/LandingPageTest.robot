*** Settings ***


Resource  ../../resources/Common.resource
Resource  ../../resources/AmazonApp.resource
Test Setup  Begin Web Test
Test Teardown  End Web Test


*** Test Cases ***
user can search for products
    [Tags]  TC-1434
    Given user is not logged in
    Then check landing page title