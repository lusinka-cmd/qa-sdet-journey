def login(user, password):
    if user == "admin" and password == "1234":
        return "Login successful"
    else:
        return "Login failed"