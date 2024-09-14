import random

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_single_quote_status_code():
    """
    Check that the quote endpoint returns a 200 status code.
    """

    response = client.get("/quotes-api/quote")

    assert response.status_code == 200


def test_quote_response_structure():
    """
    Check the structure of the quote that is retuned.
    """

    response = client.get("/quotes-api/quote")
    quote = response.json()["quote"]

    # Check that the `quote` and `author` keys exist in the response JSON
    assert "quote" in quote.keys()
    assert "author" in quote.keys()

    # Check that the quote text and author name are greater than 0 characters
    assert len(quote["quote"]) > 0
    assert len(quote["author"]) > 0


def test_multiple_quotes_status_code():
    """
    Check that the quotes endpoint returns a 200 status code
    """

    response = client.get("/quotes-api/quotes")

    assert response.status_code == 200


def test_multiple_quotes_limit():
    """
    Check that the quotes endpoint returns 10 quotes by default and
        that the `limit` query parameter can be changed.
    """

    # Default limit of 10
    response = client.get("/quotes-api/quotes")
    assert len(response.json()["quotes"]) == 10

    # Change the limit
    response = client.get("/quotes-api/quotes", params={"limit": 20})
    assert len(response.json()["quotes"]) == 20


def test_list_authors():
    """
    Check that the list of authors are returned
    """

    response = client.get("/quotes-api/authors")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_quotes_by_authors():
    """
    Check that quotes can be retrieved by their author.
    """

    # Get the list of valid authors
    authors_response = client.get("/quotes-api/authors")
    authors_list = authors_response.json()

    # Test using an author's name in the same spelling as it was retrieved from the API
    # (Don't uppercase or lowercase the name)
    name = random.choice(authors_list)
    response = client.get(f"/quotes-api/quotes/{name}")

    assert response.status_code == 200
    assert len(response.json()) > 0

    # Test using an author's name in all uppercase
    name = random.choice(authors_list)
    response = client.get(f"/quotes-api/quotes/{name.upper()}")

    assert response.status_code == 200
    assert len(response.json()) > 0

    # Test using an author's name in all lowercase
    name = random.choice(authors_list)
    response = client.get(f"/quotes-api/quotes/{name.lower()}")

    assert response.status_code == 200
    assert len(response.json()) > 0

    # Test using a non-existent author
    name = "Darth Vader"
    response = client.get(f"/quotes-api/quotes/{name}")

    assert response.status_code == 200
    assert len(response.json()) == 0
