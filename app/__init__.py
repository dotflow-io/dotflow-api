"""API __init__ module."""

__version__ = "0.1.0"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from app import __version__
from app.api.ping import ping_router
from app.api.v1.routers import v1


app = FastAPI(
    title="Dotflow",
    description="Dotflow API",
    contact={
        "name": "Fernando Celmer",
        "email": "email@fernandocelmer.com",
    },
    version=__version__
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_app():
    """Create a FastAPI app"""

    app.include_router(ping_router, prefix="/ping")
    app.include_router(v1, prefix="/v1")

    FastAPIInstrumentor.instrument_app(app)

    return app
