import json
import random

import secure
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Quotes API", description="API that returns random quotes", version="0.0.1"
)
secure_headers = secure.Secure()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


class Quote(BaseModel):
    quote: str
    author: str


class SingleQuoteResponse(BaseModel):
    quote: Quote


class MultipleQuoteResponse(BaseModel):
    quotes: list[Quote]


@app.get("/quotes-api/healthcheck", status_code=200, tags=["healthcheck"])
async def healthcheck():
    return {"status": "up"}


with open("./quotes.json", "r") as json_file:
    quotes = json.load(json_file)["quotes"]


@app.get("/quotes-api/quote")
async def get_single_quote() -> Quote:
    """Picks a random quote from the quotes.json file and returns it.

    Returns:
        dict: Random quote and its author
    """
    random_quote = random.choice(quotes)

    return Quote(**random_quote)


@app.get("/quotes-api/quotes")
async def get_multiple_quotes(limit: int = 10) -> list[Quote]:
    """Picks multiple random quotes from the quotes.json file (up to the `limit`)
    and returns those.

    Args:
        limit (int, optional): The max number of quotes to return. Defaults to 10.
    """

    return [Quote(**quote) for quote in random.sample(quotes, limit)]


@app.get("/quotes-api/quotes/{author}")
async def get_quotes_by_author(author: str) -> list[str] | list:
    """Return all of the quotes by the provided author.

    Args:
        author (str): Author to search for.

    Returns:
        list[str] | list: All quotes by this author or None if there are
            no quotes by this author.
    """

    authors_quotes = []

    for quote in quotes:
        if quote["author"].lower() == author.lower():
            authors_quotes.append(quote["quote"])

    return authors_quotes


@app.get("/quotes-api/authors")
async def list_authors() -> list[str]:
    """Returns a list of all unique quote authors.

    Returns:
        list[str]: List of unique authors
    """

    authors = {quote["author"] for quote in quotes}
    authors = list(authors)
    authors.sort()

    return authors
