#!/user/bin/env python3
"""This module contains the views for the kore app.

@File: corehttp.py
@Version: 0.3.0 to 0.3.0.?
@Desc: apps | kore | http
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/13
@Date Modified: 23/09/13
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
@Changelog:

 AI Instructions:
1) Create, and complete from the following boilerplate a BDD
test for the contact form using django Behave/Behave, and inportion to the
correct files

2) Refer to be following paths of the projects:
    - apps/core/**.py

    Feature: Contact Form
        An anonymous user creates messages to contact the site owner and
        sends the message using a form and via email.

    Scenario: An anonymous user creates messages to contact the site owner
        Given I am an anonymous user
        When I visit the index page
        And I navigate to the contact form on the index page
        And I fill in the contact form
        And I submit the contact form
        Then  the Status code is 200
        And I should see the message "Thank you for your message.
        It has been sent."
"""

import behave

from django.test import Client
from django.urls import reverse

from apps.kore.values import HTTP


class MessageSite:
    """Feature: Contact Form"""

    class Scenario:
        """Scenario: An anonymous user creates messages
        to contact the site owner
        """

        class Given:
            """Given I am an anonymous user."""
            GIVEN1 = 'I am an anonymous user'

        class When:
            """When I visit the index page."""
            WHEN1 = 'I visit the index page'
            WHEN2 = 'I navigate to the contact form on the index page'
            WHEN3 = 'I fill in the contact form'
            WHEN4 = 'I submit the contact form'

        class Then:
            """Then  the Status code is 200."""
            THEN1 = 'the Status code is 200'
            THEN2 = 'I should see the message ' \
                    "\"Thank you for your message. It has been sent.\""

    class ASSERTS:
        """ASSERTS Strings.

        Assertion Constants.
        """
        STATUS = HTTP.STATUS.OK
        MESSAGE = 'Thank you for your message. It has been sent.'
        FORM = 'contact_form'

    class CTX:
        """CTX Strings.

        Test Context
        """
        INDEX = 'index'
        CLIENT = 'client'
        RESPONSE = 'response'
        DATA = {'name': 'Test Name',
                'email': 'test@example.com',
                'message': 'This is a test message'}
        FORMVIEW = 'submit_contact_form'
        FORMNAME = 'contact_form'


behave.use_step_matcher('re')


# noinspection PyUnusedFunction
@behave.given(MessageSite.Scenario.Given.GIVEN1)
def step_impl(context):
    """Feature: MessageSute.feature

    Given I am an anonymous user
    Arrange: Load a client
    """
    context.client = Client()


# noinspection PyUnusedFunction
@behave.when(MessageSite.Scenario.When.WHEN1)
def step_impl(context):
    """Feature: MessageSute.feature

    Given I am an anonymous user
    Arrange: Load a client
    """
    # replace 'index' with the name of your index page view
    context.response = (
        context.client.get(reverse(
            MessageSite.CTX.INDEX)))


# noinspection PyUnusedFunction
@behave.when(MessageSite.Scenario.When.WHEN2)
def step_impl(context):
    """Feature: MessageSute.feature

    When I navigate to the fomr
    Act: Find the form.
    """
    # Ensure the form exists in the index page
    assert (MessageSite.ASSERTS.FORM in
            context.response.content.decode())


# noinspection PyUnusedFunction
@behave.when(MessageSite.Scenario.When.WHEN3)
def step_impl(context):
    """Feature: MessageSute.feature

    When I enter data
    Act: Fill in the form
    """
    context.data = MessageSite.CTX.DATA


# noinspection PyUnusedFunction
@behave.when(MessageSite.Scenario.When.WHEN4)
def step_impl(context):
    """Feature: MessageSute.feature

    When I submit
    Act: Send a message
    """
    context.response = \
        context.client.post(reverse(MessageSite.CTX.FORMVIEW,
                                    context.data))
    # replace 'submit_contact_form' with the name of your contact
    # form submission view


# noinspection PyUnusedFunction
@behave.then(MessageSite.Scenario.Then.THEN1)
def step_impl(context):
    """Feature: MessageSute.feature

    Given I am an anonymous user
    Assert: Expect a status code
    """
    assert (context.response.status_code ==
            MessageSite.ASSERTS.STATUS)


# noinspection PyUnusedFunction
@behave.then(MessageSite.Scenario.Then.THEN2)
def step_impl(context):
    """Feature: MessageSute.feature

    Then get a feedback
    Assert: Cofirmation
    """
    assert (MessageSite.ASSERTS.MESSAGE in
            context.response.content.decode())
