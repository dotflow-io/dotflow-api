"""Routers"""

from fastapi import APIRouter
from app.api.v1.endpoints import router_workflow
from app.api.v1.endpoints import router_task


v1 = APIRouter()

v1.include_router(router_workflow, tags=["Workflow"])
v1.include_router(router_task, tags=["Task"])
