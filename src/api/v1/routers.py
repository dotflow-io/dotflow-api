"""Routers"""

from fastapi import APIRouter
from src.api.v1.endpoints import workflow
from src.api.v1.endpoints import task


v1 = APIRouter()
v1.include_router(workflow.router, tags=["Workflow"])
v1.include_router(task.router, tags=["Task"])
