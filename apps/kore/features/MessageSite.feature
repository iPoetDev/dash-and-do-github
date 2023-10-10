# Created by Charles at 16 Sep 2023
Feature: Messaging the Site
  All users can send messages to the site owner via a contact form on the home page.

  Scenario: Messaging the site without CC
    Given Bob is a user
    When Bob fills in the contact form on the said page without requesting a CC
    And Bob submits the contact form
    Then a confirmation message should be displayed to Bob
    And a message should be sent via email to the owner

  Scenario: Messaging the site with CC
    Given Bob is a user
    When Bob fills in the contact form on the said page with a request for a CC
    And Bob submits the contact form
    Then a confirmation message should be displayed to Bob
    And a message should be sent via email to the owner
    And a copy of the message should be sent via email to Bob

  Scenario: Owner receiving the contact form message
    Given Alice is the site owner
    When Alice receives an email from the site
    Then the email contains a templated message from the contact form

  Scenario: Email not sent error
    Given Bob is a user
    When Bob fills in the contact form and submits
    But the email cannot be sent due to an error
    Then an error message should be displayed to Bob notifying him that the email was not sent

  Scenario: Email provider offline error
    Given Bob is a user and Alice is the site owner
    When Bob fills in the contact form and submits
    But the email cannot be sent because the email provider is offline
    Then An error message should be displayed to Bob
    And Alice is notifying about the offline status
