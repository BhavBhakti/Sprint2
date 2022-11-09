Feature: Flipkart Login
  Scenario Outline: : Login data
    Given we navigate to Flipkart url
    When we validate the mobile number text
    And we type in the "<number>" edit box
    And we validate the password text
    And we type in the "<password>" field
    And we click on the login button
    Examples:
      | number | password |
    | 8867181165 | Bhavika@123 |