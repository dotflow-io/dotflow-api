"""Task endpoint"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.errors import TaskNotFoundException
from app.services.task_service import TaskService


router_task = APIRouter()


@router_task.get("/tasks", response_model=List[None])
def get_all(
    offset: int = 0,
    limit: int = 100,
    sort_by: str = "id",
    order_by: str = "desc",
    service: TaskService = Depends(TaskService)
):
    return service.get_all(
        offset=offset,
        limit=limit,
        sort_by=sort_by,
        order_by=order_by,
    )


@router_task.get("/tasks/{model_id}", response_model=None)
def get_one(model_id: int, service: TaskService = Depends(TaskService)):
    try:
        return service.get_one(
            model_id=model_id
        )
    except TaskNotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error


@router_task.put("/tasks", response_model=None)
async def update(
    model_id: int,
    data: dict,
    service: TaskService = Depends(TaskService)
):
    try:
        return service.update(
            data=data.model_dump(),
            model_id=model_id
        )
    except TaskNotFoundException as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        ) from error


@router_task.post(
    "/tasks", response_model=None, status_code=status.HTTP_201_CREATED)
async def create(
    data: dict,
    service: TaskService = Depends(TaskService)
):
    return service.create(data=data.model_dump())
