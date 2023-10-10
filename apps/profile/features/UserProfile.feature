Feature: User Profile Management
"""
  Title: User Profile Management
  Description: Managing user profiles in Dash and Do, including integrations and account deletions
  Style: Narrative, Declarative, not Imperative/Procedural
"""

  Scenario: Bob wants to view his profile
    Given the Dash and Do web application
    When Bob chooses to view his profile
    Then Dash and Do should display Bob's profile

  Scenario: Bob updates his profile
    Given Bob has chosen to update his profile on Dash and Do
    When Bob submits his updated details
    Then Dash and Do should reflect the changes on Bob's profile

  Scenario: Bob connects his account to GitHub
    Given Bob wants to connect his account to GitHub on Dash and Do
    When Bob successfully authenticates via GitHub
    Then Dash and Do should link Bob's GitHub account to his Dash and Do profile
    And Dash and Do should reflect this linkage on Bob's profile

  Scenario: Bob disconnects his account from GitHub
    Given Bob wants to disconnect his account from GitHub on Dash and Do
    When Bob disconnects from GitHub
    Then Dash and Do should unlink Bob's GitHub account from his Dash and Do profile
    And Dash and Do should reflect this change on Bob's profile

  Scenario: Bob deletes his account
    Given Bob wants to delete his account on Dash and Do
    When Bob confirms account deletion
    Then Dash and Do should permanently delete Bob's account
    And Dash and Do should confirm the account deletion to Bob
