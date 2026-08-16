import requests

BASE_URL = "https://api.github.com"
REPOSITORY = "octocat/Hello-World"
TIMEOUT_SECONDS = 10
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "qa-sdet-portfolio-tests",
}


def get_repository():
    return requests.get(
        f"{BASE_URL}/repos/{REPOSITORY}",
        headers=HEADERS,
        timeout=TIMEOUT_SECONDS,
    )


def test_get_repository_returns_successful_response():
    response = get_repository()

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")


def test_repository_response_matches_expected_schema():
    response = get_repository()
    response.raise_for_status()

    repository = response.json()
    required_fields = {"id", "name", "full_name", "private", "html_url"}

    assert required_fields.issubset(repository)
    assert isinstance(repository["id"], int)
    assert repository["name"] == "Hello-World"
    assert repository["full_name"] == REPOSITORY
    assert repository["private"] is False
    assert repository["html_url"].startswith("https://github.com/")
