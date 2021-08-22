from socket import gethostname

from fastapi import APIRouter


router = APIRouter(tags=["Healthcheck"])


@router.get("/healthcheck", status_code=200)
async def healthcheck():
    return {"status": 'healthy', 'hostname': gethostname()}

