def login(username: str, password: str) -> bool:
    """Return whether the supplied credentials match the expected test user."""
    return username == "admin" and password == "1234"
