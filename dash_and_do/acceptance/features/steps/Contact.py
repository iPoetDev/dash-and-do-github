from behave import *
from django.test import Client
from django.urls import reverse

use_step_matcher("re")

""" AI Instriuctions:
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
        And I should see the message "Thank you for your message. It has been sent."
"""


# noinspection PyUnusedFunction
@given("I am an anonymous user")
def step_impl(context):
    context.client = Client()


# noinspection PyUnusedFunction
@when("I visit the index page")
def step_impl(context):
    context.response = context.client.get(reverse(
        'index'))  # replace 'index' with the name of your index page view


# noinspection PyUnusedFunction
@when("I navigate to the contact form on the index page")
def step_impl(context):
    # Ensure the form exists in the index page
    assert 'contact' in context.response.content.decode()


# noinspection PyUnusedFunction
@when("I fill in the contact form")
def step_impl(context):
    context.data = {'name': 'Test Name', 'email': 'test@example.com',
                    'message': 'This is a test message'}


# noinspection PyUnusedFunction
@when("I submit the contact form")
def step_impl(context):
    context.response = context.client.post(reverse('submit_contact_form'),
                                           context.data)  # replace 'submit_contact_form' with the name of your contact form submission view


# noinspection PyUnusedFunction
@then("the Status code is 200")
def step_impl(context):
    assert context.response.status_code == 200


# noinspection PyUnusedFunction
@then(
    'I should see the message "Thank you for your message. It has been sent."')
def step_impl(context):
    assert 'Thank you for your message. It has been sent.' in context.response.content.decode()
