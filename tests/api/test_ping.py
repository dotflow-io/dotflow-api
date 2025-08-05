"""Tests for ping views."""

# pylint: disable-all
# pylint: skip-file
# flake8: noqa
# pylint: disable=redefined-outer-name

from unittest import TestCase

import pytest

from fastapi import status

from tests.conftest import test_client


class TestEnpointPing(TestCase):
    """Test class for ping endpoint."""

    URL_BASE = "/ping/"

    @pytest.fixture(autouse=True)
    def prepare_fixture(self, test_client):
        """Fixture to prepare the test client for each test."""
        self.test_client = test_client

    def test_ping(self):
        """Test the ping endpoint."""
        response = self.test_client.get(self.URL_BASE)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'status': "it's alive"})
