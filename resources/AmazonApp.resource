*** Settings ***
Resource  ../PageObjects/LandingPage.resource
Resource  ../PageObjects/TopNav.resource
Resource  ../PageObjects/SearchResults.resource
Resource  ../PageObjects/Product.resource
Resource  ../PageObjects/Cart.resource
Resource  ../PageObjects/SignIn.resource

*** Keywords ***
user is not logged in
    Log  Check to see whether user is logged in

check landing page title
    LandingPage.Verify Page Loaded

user searches for products
    LandingPage.Load
    TopNav.Search for Products

search results contains relevant products
    SearchResults.Verify Search Completed

user selects a product from search results
    SearchResults.Click Product link
    Product.Verify Page Loaded

user selects a searched product
    [Documentation]  This 2nd level keyword calls other 1st level keywords to help simplify the test case
    user searches for products
    search results contains relevant products
    user selects a product from search results

correct product page loads
    Product.Verify Page Loaded

user adds that product to their cart
    Product.Add to Cart

user adds a product to their cart

    user searches for products
    search results contains relevant products
    user selects a product from search results
    correct product page loads
    user adds that product to their cart
    the product is present in cart

the product is present in cart
    Cart.Verify Product Added

user click on checkout
    Cart.Proceed to Checkout

user should sign in to their account
    SignIn.Verify Page Loaded

the user navigates to cart
    Cart.proceed to cart
    Cart.Go to Cart

the user deletes the item from the list
    cart.delete item from cart

cart is empty
    cart.verify cart is empty
