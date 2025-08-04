"""Task endpoint"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks", status_code=200)
async def get():
    return []


@router.get("/tasks/{id}", status_code=200)
def get_by_id(id: int):
    return {}


@router.post("/tasks", status_code=201)
async def post():
    return {}
