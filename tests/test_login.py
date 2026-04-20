import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from login_check import login
from login_check import login

def test_login_success():
    result = login("admin", "1234")
    assert result == "Login successful"
def test_login_wrong_password():
    result = login("admin", "wrong")
    assert result == "Login failed"