"""Module defining a test instance of the API client.

The test client will have all the required dependencies overridden with the test equivalent.
"""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from src.main import main_app


@pytest.fixture
def fastapi_test_client() -> Generator[None, None, TestClient]:
    """Test FastAPI client.

    Use this to make requests to endpoints.
    Example:
        fastapi_test_client.get("/health-check")
    """
    return TestClient(main_app)
