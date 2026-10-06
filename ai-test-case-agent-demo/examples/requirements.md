# Login requirements (synthetic demo data)

1. A user with valid credentials can sign in and sees the Products page.
2. Invalid credentials are rejected and a clear error message is displayed.
3. A locked user cannot sign in and sees an account-locked message.
4. The password field must not display the entered password as plain text.

The sample environment uses a pytest `page` fixture and Playwright's synchronous Python API. Login form selectors and exact messages must be confirmed against the real application before using any generated test.
