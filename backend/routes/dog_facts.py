from typing import Optional

from fastapi import APIRouter
import httpx


router = APIRouter(tags=["Dog facts"])


@router.get("/dogfacts")
async def dog_facts(facts_limit: Optional[int] = 10):
    response = httpx.get(
        "http://dog-api.kinduff.com/api/facts", params={"number": facts_limit}
    )
    return {"Dog facts": response.json()["facts"]}
