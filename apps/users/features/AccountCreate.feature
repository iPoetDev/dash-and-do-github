Feature: Account Creation
"""
  Title: Account Creation
  Description: User registration and signup for Dash and Do
  Style: Narrative, Decalrative, not Imperative/Procedural
"""

  Scenario: Bob wants to register
    Given the Dash and Do web application
    When Bob chooses to register
    Then Bob should be able to enter his details for account creation

  Scenario: Bob successfully creates an Account
    Given Bob has entered all required valid details for registration on Dash and Do
    When Bob submits his details
    Then Dash and Do should create a new account for Bob
    And Dash and Do should direct Bob to the home page

  Scenario: Bob is notified about the email confirmation
    Given Bob has successfully registered on Dash and Do
    When Bob's registration is processed
    Then Dash and Do should send a confirmation email to Bob
    And Dash and Do should notify Bob to check his email for confirmation

  Scenario: Bob requests for a new confirmation email
    Given Bob did not receive the confirmation email
    When Bob requests for a new confirmation email
    Then Dash and Do should resend a confirmation email to Bob

  Scenario: Bob successfully confirms his Account
    Given Bob has received a confirmation email
    When Bob clicks on the confirmation link
    Then Dash and Do should confirm Bob's account
    And Dash and Do should redirect Bob to the verification success page

  Scenario: Bob fails in Account Confirmation
    Given Bob has a confirmation email
    When Bob tries to confirm his account but the confirmation process fails
    Then Dash and Do should display an error message to Bob

  Scenario: Bob tries to create an account with an existing email
    Given Bob uses an existing email to register on Dash and Do
    When Bob submits the registration form
    Then Dash and Do should not create a new account
    And Dash and Do should notify Bob that the email is already registered

  Scenario: Bob provides invalid details for account creation
    Given Bob has provided invalid details for account creation
    When Bob attempts to register on Dash and Do
    Then Dash and Do should not create an account for Bob
    And Dash and Do should notify Bob that the details provided are incorrect

  @same_email @manual
  Scenario: Bob tries to create a second account after creating one
    Given Bob has created an account on Dash and Do
    When Bob tries to create another account with same email
    Then Dash and Do should not create a new account for Bob
    And Dash and Do should notify Bob that he already has an account
    But Dash and Do should notify error messages to Bob

  @different_email @manual
  Scenario: Bob tries to create a second account after creating one
    Given Bob has created an account on Dash and Do
    When Bob tries to create another account with a different email
    Then Dash and Do should create a new account for Bob
    But Dasn and Do should not notify error messages to Bob
