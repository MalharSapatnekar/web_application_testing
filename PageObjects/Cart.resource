*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Verify Product Added
    Wait Until Page Contains  Added to Cart

Proceed to Checkout
    Click Element  //input[@value="Proceed to checkout"]

Proceed to Cart
    click element    xpath=//span[@id="sw-gtc"]

Go to Cart
    wait until page contains    Shopping Cart
    #wait until page contains    Deselect all items

Delete item from cart
    click element    xpath=//input[@value="Delete"]

Verify Cart is empty
    wait until page contains    Your Amazon Cart is empty