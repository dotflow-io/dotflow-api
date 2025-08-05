"""Workflow endpoint"""

from fastapi import APIRouter

router_workflow = APIRouter()


@router_workflow.get("/workflows", status_code=200)
async def get():
    return []


@router_workflow.get("/workflows/{id}", status_code=200)
def get_by_id(id: int):
    return {}


@router_workflow.post("/workflows", status_code=201)
async def post():
    return {}
