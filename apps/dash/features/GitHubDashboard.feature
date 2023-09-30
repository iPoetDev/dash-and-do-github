Feature: Github Repository Dashboard
"""
  Title: Github Repository Dashboard
  Description: Fetch, read, list and read a User's Github repositories properties and state as a
  dashboard, with the ability to view all repository's details on a single page.
  Style: Narrative, Declarative, not Imperative/Procedural
"""

  Scenario: User's access to Github Dashboard
    Given Bob is a recognized Github user
    When Bob attempts to view the "Github Repository Dashboard" page
    Then the system validates Bob's access rights

  Scenario: Displaying Dashboard Page
    Given Bob has been granted access to the "Github Repository Dashboard" page
    When Bob navigates to the "Github Repository Dashboard"
    Then a table should be visible on the Dashboard page

  Scenario: Listing User's Github Repositories
    Given Bob is on the "Github Repository Dashboard" page
    And Bob has access rights
    Then all of Bob's Github repositories should be displayed in the table

  Scenario: Viewing repository details
    Given Bob is viewing the table of his Github repositories on the Dashboard page
    Then each column of the table presents the repository properties
    And each row of the table represents a repository
    # name, description, owner, last commit date, main language, and the number of stars the repository has garnered

  Scenario: User with no Github Repositories
    Given Bob is a recognized Github user
    But Bob has no Github repositories
    When Bob views the "Github Repository Dashboard" page
    Then a message "No repositories found" should be displayed.

  Scenario: Inaccessible Repository due to Permission Changes
    Given a Github repository "Repo1" that Bob no longer has access to
    When Bob explores the "Github Repository Dashboard" page
    Then "Repo1" does not appear in the listed repositories
    And Bob is notified that "Some repositories are no longer accessible"

  Scenario: Inaccessible Repository due to Deletion
    Given a deleted Github repository, previously accessible by Bob
    When Bob explores the "Github Repository Dashboard" page
    Then the deleted repository is absent from the list
    And Bob is notified that "Some repositories are no longer accessible"

  Scenario: User's Repositories are Inaccessible
    Given Bob's Github repositories are all inaccessible
    When Bob explores the "Github Repository Dashboard" page
    Then a notification "No repositories found" is displayed to Bob
