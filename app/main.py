from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.api.v1.routers import v1


app = FastAPI(
    title="Dotflow",
    description="Dotflow API",
    version=__version__
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1, prefix="/v1")


@app.get("/status", include_in_schema=False)
def get_status():
    """Get status of messaging server."""
    return {"status": "it's alive"}
