import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pages.google_page import GooglePage

def test_google_search(page):
    google = GooglePage(page)

    google.open()
    google.search("Playwright")

    page.wait_for_timeout(3000)

    assert "Playwright" in google.get_title()