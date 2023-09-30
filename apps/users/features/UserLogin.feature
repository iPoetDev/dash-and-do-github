Feature: User Login
"""
  Title: User Login
  Description: Existing user login to Dash and Do
  Style: Narrative, Declarative, not Imperative/Procedural
"""

  Scenario: Bob wants to Login
    Given the Dash and Do web application
    When Bob chooses to login
    Then Bob should be able to enter his credentials

  Scenario: Bob successfully Logs In
    Given Bob has entered his correct credentials on Dash and Do
    When Bob submits his credentials
    Then Dash and Do should verify the credentials
    And Dash and Do should direct Bob to the home page

  Scenario: Bob fails to Login
    Given Bob has entered incorrect credentials
    When Bob attempts to login to Dash and Do
    Then Dash and Do should not authenticate Bob
    And Dash and Do should notify Bob that the entered credentials are incorrect

  Scenario: Bob forgot password
    Given Bob forgot his password
    When Bob chooses forgot password option
    Then Dash and Do should initiate a reset password workflow
    And Dash and Do should notify Bob to check his email for reset password instructions

  Scenario: Bob resets password
    Given Bob has received a reset password email
    When Bob follows the reset password instructions
    Then Dash and Do should allow Bob to reset his password
    And Dash and Do should direct Bob to login with his new credentials

  Scenario: Bob locks his account after multiple unsuccessful login attempts
    Given Bob has entered incorrect credentials multiple times
    When Bob attempts to login again
    Then Dash and Do should lock Bob's account temporarily
    And Dash and Do should notify Bob about the account lock
