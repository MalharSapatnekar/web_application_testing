*** Settings ***


Resource  ../../resources/Common.resource
Resource  ../../resources/AmazonApp.resource
Test Setup  Begin Web Test
Test Teardown  End Web Test


*** Test Cases ***

user can add product to cart, View Cart and Add More Products to the cart
    [Tags]  TC-1433
    Given user is not logged in
    And user searches for products
    And search results contains relevant products
    And user selects a product from search results
    And correct product page loads
    And user adds that product to their cart
    And the product is present in cart
    When user click on checkout
    Then user should sign in to their account