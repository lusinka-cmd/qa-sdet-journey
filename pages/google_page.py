class GooglePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://www.google.com")

    def search(self, text):
        self.page.fill("textarea[name='q']", text)
        self.page.press("textarea[name='q']", "Enter")

    def get_title(self):
        return self.page.title()