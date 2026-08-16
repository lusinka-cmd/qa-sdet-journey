import pytest

from login_check import login


@pytest.mark.parametrize(
    ("username", "password"),
    [
        ("admin", "1234"),
    ],
)
def test_login_accepts_valid_credentials(username, password):
    assert login(username, password) is True


@pytest.mark.parametrize(
    ("username", "password"),
    [
        ("admin", "wrong-password"),
        ("unknown-user", "1234"),
        ("", ""),
    ],
)
def test_login_rejects_invalid_credentials(username, password):
    assert login(username, password) is False
