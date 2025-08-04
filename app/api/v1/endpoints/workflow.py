"""Workflow endpoint"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/workflows", status_code=200)
async def get():
    return []


@router.get("/workflows/{id}", status_code=200)
def get_by_id(id: int):
    return {}


@router.post("/workflows", status_code=201)
async def post():
    return {}
