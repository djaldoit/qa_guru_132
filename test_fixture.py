import pytest

@pytest.fixture
def login_page(browser):
    print("Login page opened")


@pytest.fixture
def user():
    print("User created")
    return "username", "password"


def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"


def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"





