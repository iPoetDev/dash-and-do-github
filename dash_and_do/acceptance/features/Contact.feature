# Created by Charles at 16 Sep 2023
Feature: Contact Form
  An anonymous user creates messages to contact the site owner and sends the message via a form and email.

  Scenario: An anonymous user creates messages to contact the site owner
    Given I am an anonymous user
    When I visit the index page
    And I navigate to the contact form on the index page
    And I fill in the contact form
    And I submit the contact form
    Then  the Status code is 200
    And I should see the message "Thank you for your message. It has been sent."

Feature: Contact Form Owner
  An site contact recieves messages, by email, from the contact form from an anonymous user.

  Scenario: The site owner recieves another email messages from the contact form
    Given I am the site owner
    When I recieve an email from the site
    And the email is from the contact form
    Then I should see templated email messages from the contact form

Feature: Contact Form CC
  An anonymous user wants a copy of the message they sent to the site owner.

  Scenario: An anonymous user wants a copy of the message they sent to the site owner.
    Given I am an anonymous user
    When I visit the index page
    And I navigate to the contact form on the index page
    And I fill in the contact form
    And I submit the contact form
    Then  the Status code is 200
    And I should see the message "Thank you for your message. It has been sent."
    And I should receive an copy of email address, with my message.
