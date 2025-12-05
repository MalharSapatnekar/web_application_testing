*** Settings ***


Resource  ../../resources/Common.resource
Resource  ../../resources/AmazonApp.resource
Test Setup  Begin Web Test
Test Teardown  End Web Test


*** Test Cases ***

user can add product to cart and View Cart
    [Tags]  TC-1431
    Given user is not logged in
    And user searches for products
    And search results contains relevant products
    And user selects a product from search results
    And correct product page loads
    When user adds that product to their cart
    Then the product is present in cart
    And the user navigates to cart