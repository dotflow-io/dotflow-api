"""Here are define pytest fixtures, hooks and plugins."""

import pytest
from fastapi.testclient import TestClient

from app import create_app

app = create_app()


@pytest.fixture
def test_client() -> TestClient:
    """Create a TestClient for testing."""
    client = TestClient(app)

    return client
