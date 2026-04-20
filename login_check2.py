def login(user, password):
    if user == "admin" and password == "1234":
        return "Login successful ✅"
    else:
        return "Login failed ❌"


print(login("admin", "1234"))
print(login("admin", "wrong"))
print(login("wrong", "1234"))
print(login("", ""))