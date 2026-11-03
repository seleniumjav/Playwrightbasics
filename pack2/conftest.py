import pytest
from playwright.sync_api import Page


@pytest.fixture(scope="class",autouse=True)
def setup():
    print("before test")
    yield
    print("after test")
