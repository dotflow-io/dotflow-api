"""Endpoints"""

from app.api.v1.endpoints.task import router_task
from app.api.v1.endpoints.workflow import router_workflow

__all__ = [
    "router_task",
    "router_workflow",
]
