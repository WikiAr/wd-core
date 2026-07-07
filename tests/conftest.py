"""
Test configuration for the test-suite.
Common fixtures for mocking API, DB, and other dependencies.
"""


import pytest
from pytest_socket import disable_socket


@pytest.fixture(autouse=True)
def stop_nets() -> None:
    disable_socket(allow_unix_socket=True)
