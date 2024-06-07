*** Settings ***


Resource  ../../resources/Common.resource
Resource  ../../resources/AmazonApp.resource
Test Setup  Begin Web Test
Test Teardown  End Web Test


*** Test Cases ***


user can view a product
    [Tags]  TC-1435
    Given user is not logged in
    And user searches for products
    And search results contains relevant products
    And user selects a product from search results
    Then correct product page loads