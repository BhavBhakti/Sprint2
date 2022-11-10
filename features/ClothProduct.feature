Feature: Flipkart Login
 Scenario Outline:  Login data
    Given we navigate to Flipkart website
    And close the window
    And we click on Login Button
    Then we give "<numberr>" edit box
    And we give the "<passwordd>" edit box
    And we click on login button
    Then type "<search>" in searchbox
    And click on search button
    Then click on Top image
    And switch to window
    Then click on all front-back images
    Then Enter "<pincode>"
    And click on check link
    Then click on all colors
    Then click on all sizes
    Then click on plus sign
    Then click on all addtocart
    Then verify placeorder button
    Examples:
       | numberr | passwordd | search | pincode |
       | 8867181165 | Bhavika@123 | Tops | 560032 |
#       | 8867181165 | Bhavika@123 | T-shirts | 560032 |
#       | 8867181165 | Bhavika@123 | women jackets | 56031 |