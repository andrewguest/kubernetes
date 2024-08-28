from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import secure

from routes.healthcheck import router as healthcheck_router
from routes.dog_facts import router as dogfacts_router


app = FastAPI(
    title="Kubernetes Example API",
    description="Kubernetes Example API",
    version="0.0.1",
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


app.include_router(healthcheck_router)
app.include_router(dogfacts_router)
