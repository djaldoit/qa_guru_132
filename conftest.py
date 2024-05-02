import pytest
@pytest.fixture(scope="module")
def browser():
    print("Browser opened")
    yield
    print("Browser closed")