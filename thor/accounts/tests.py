"""
This file contains the tests for the accounts module.
Run './manage.py test accounts' to run the test suite
"""
from django.test import TestCase
from django.test.utils import override_settings

# Import the custom built user classes for testing
from accounts import MyUserManager, CustomUser
