#!/user/bin/env python3
"""@File: emails.py
@Version: 0.3.0 to 0.3.1: Test Email sending
@Desc: apps | kore |  emailing | tests
@Author: Charles Fowler
@Copyright: 2023
@Date Created: 23/09/12
@Date Modified: 23/09/12
@Python Version: 3.11.04
@Django Version: 4.2.3
@Notes / Ideas v Implement:
- Test Email sending
- Use various emailing backends
@Changelog:
- Added:
- 23/09/19: Added docstrings
- 23/09/19: Created initial file
- 23/09/19: added MailPanel tests for emailing *
- 23/09/19: Adding Refactored test
case
- Updated:
- 23/09/19: Refactored Functions into messages.py and helpers.py
- 23/09/13: Refactored Imports ...
to reduce file level cycolmatic complexity
- Deprecated:
- 23/09/19: Deprecated
- Removed:
- 23/09/19: Removed
@Plan:
- TODO:
- Create test cases for models.
- Define Test Scenarios
- Happy Path
- Edge Cases
- Other
"""
#  Copyright (c) 2023.
# Python
import logging

from unittest import mock

# Django
from django.core import mail
from django.test import Client
from django.test import TestCase
from django.test.utils import override_settings

# OopCompanion:suppressRename

# Default: Django's SMTP
# noinspection PyUnusedName
DJSTMP_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# noinspection PyUnusedName
STMP_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Use for development only: to stdout, only
# noinspection PyUnusedName
DJCONSOLE_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DJ Test Runner uses this for testing
# noinspection PyUnusedName
DJMEMORY_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
# noinspection PyUnusedName
DJDUMMY_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
# noinspection PyUnusedName
ANYJET_BACKEND = 'anymail.backends.mailjet.EmailBackend'
MAILPANEL_BACKEND = 'mail_panel.backend.MailToolbarBackend'

# Send Mail
PATCH_DJSENDMAIL = 'django.core.mail.send_mail'
# noinspection PyUnusedName
PATCH_ANYMAIL = 'anymail.message.AnymailMessage.send'
# Client
PATCH_CLIENT = 'django.test.Client'


class TestEmail(TestCase):
    """TestEmail that tests & mocks the functionality of sending an emailing
    using Django Unittest.

    :class: TestEmail :method: setUpTestData: Setup once per class
    :method: setUp: Set once per method :method: test_send_email
    :method: mock_test_send_email
    """

    @classmethod
    def setUpTestData(cls):
        """Setup for tests.

        :method: setUpTestData
        :return:
        """
        cls.client = Client()
        cls.email_data = {
            'limit': 1,
            'name': 'test',
            'emailing': 'charlesjfowler@outlook.com',
            'subject': 'DD: Test Email',
            'message': 'Hello, World!'
        }
        cls.route = '/contact/'
        cls.status = {
            'success': 200,
            'bad_request': 400,
            'server_error': 500,
        }
        cls.exception_msg = {
            'generic': 'An error occurred: ',
        }
        cls.email_asserts = {
            'limit': 1,
            'subject': 'Hello',
            'msg': 'Hello, World!',
            'expect_200': 'Expected status code to be 200',
            'expect_400': 'Expected status code to be 400',
            'expect_500': 'Expected status code to be 500',
            'expect_limit': 'Expected one emailing in the outbox',
            'expect_subject': 'Expected emailing subject to be "Hello"',
        }

    def setUp(self):
        """Setup for tests.

        :method: setUp
        :return:
        """
        self.setUpTestData()

    @override_settings(EMAIL_BACKEND=MAILPANEL_BACKEND)
    def test_send_email(self):
        """# HAPPY PATH

        Test send emailing: Simple Test Send Function (no mocking)
        & * Console, Logging
        :method: test_send_email
        :raises: AssertionError
        """
        try:
            # ASSERT: Check Status Code is 200
            response = self.client.post(self.route,
                                        self.email_data)
            self.assertEqual(response.status_code, self.status[ 'success' ])
            # ASSERT: Check emailing has been sent
            self.assertEqual(len(mail.outbox), self.email_asserts[ 'limit' ])
            # ASSERT: Check content of the sent emailing
            self.assertEqual(mail.outbox[ 0 ].subject,
                             self.email_asserts[ 'subject' ])

        except AssertionError as asserts:
            logging.error(f"{self.exception_msg[ 'general' ]}: {asserts}")

    @mock.patch(PATCH_DJSENDMAIL)
    @override_settings(EMAIL_BACKEND=MAILPANEL_BACKEND)
    def test_mock_send_email(self, mock_send_mail):
        """# HAPPY PATH Mock Sending a test emailing.

        :param: self:
        :param mock_send_mail:
        """
        # ACT Email Response: Via a route and emailing data
        response = self.client.post(self.route,
                                    self.email_data)

        # ASSERT: Check Status Code is 200
        self.assertEqual(response.status_code,
                         self.status[ 'success' ],
                         self.email_asserts[ 'expect_200' ])

        # ARRANGE: Check mock_send_mail method was called once
        mock_send_mail.assert_called_once()

        # ASSERT: Check emailing has been sent
        self.assertEqual(len(mail.outbox),
                         self.email_asserts[ 'limit' ],
                         self.email_asserts[ 'expect_limit' ])

        # ASSERT: Check content of the sent emailing
        self.assertEqual(mail.outbox[ 0 ].subject,
                         self.email_data[ 'subject' ],
                         self.email_asserts[ 'expect_subject' ])

    @mock.patch(PATCH_DJSENDMAIL)
    @mock.patch(PATCH_CLIENT)
    @override_settings(EMAIL_BACKEND=MAILPANEL_BACKEND)
    def test_mock_send_email_test_client(self, mock_client, mock_send_mail):
        """# HAPPY PATH Mock Sending a test emailing with valid values.

        :param self:
        :param mock_client:
        :param mock_send_mail:
        """
        # ARRANGE
        mock_client.return_value.post.return_value = \
            mock.Mock(status_code=self.status[ 'success' ])

        # ACT Email Response: Via a route and emailing data
        response = self.client.post(self.route,
                                    self.email_data)

        # ASSERT: Check Status Code is 200
        self.assertEqual(response.status_code,
                         self.status[ 'success' ],
                         self.email_asserts[ 'expect_200' ])

        # ASSERT: Check mock_send_mail method was called once
        mock_send_mail.assert_called_once()

        # ASSERT: Check emailing has been sent
        self.assertEqual(len(mail.outbox), self.email_asserts[ 'limit' ],
                         self.email_asserts[ 'expect_limit' ])

        # ASSERT: Check content of the sent emailing
        self.assertEqual(mail.outbox[ 0 ].subject,
                         self.email_data[ 'subject' ],
                         self.email_asserts[ 'expect_subject' ])

    @mock.patch(PATCH_DJSENDMAIL)  # Email Client/Send
    @mock.patch(PATCH_CLIENT)  # Test Client
    def test_mock_send_email_valid_data(self,
                                        mock_client,
                                        mock_send_mail):
        """# HAPPY PATH Mock Sending a test emailing with valid values.

        :param self:
        :param mock_client:
        :param mock_send_mail:
        :return:
        """
        # ARRANGE
        mock_client.return_value.post.return_value = \
            mock.Mock(status_code=self.status[ 'success' ])

        # ACT
        response = self.client.post(self.route, self.email_data)

        # ASSERT: Check Status Code is 200
        self.assertEqual(response.status_code,
                         self.status[ 'success' ], self.
                         email_asserts[ 'expect_200' ])

        # ASSERT: Check mock_send_mail method was called once ONLY
        mock_send_mail.assert_called_once()

        # ASSERT: Check emailing has been sent
        self.assertEqual(len(mail.outbox),
                         self.email_asserts[ 'limit' ],
                         self.email_asserts[ 'expect_limit' ])

        # ASSERT: Check content of the sent emailing
        self.assertEqual(mail.outbox[ 0 ].subject,
                         self.email_data[ 'subject' ],
                         self.email_asserts[ 'expect_subject' ])
