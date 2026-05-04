"""
Test configuration for the test-suite.
Common fixtures for mocking API, DB, and other dependencies.
"""

import sys
from unittest.mock import MagicMock, patch

import pytest

from pytest_socket import disable_socket


@pytest.fixture(autouse=True)
def stop_nets():
    disable_socket(allow_unix_socket=True)
