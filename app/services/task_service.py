"""Task Service"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.errors import TaskNotFoundException
from app.repository.task_repository import TaskRepository


class TaskService:

    def __init__(self, repository: Session = Depends(TaskRepository)):
        self.repository = repository

    def get_all(
        self,
        offset: int = 0,
        limit: int = 100,
        sort_by: str = "id",
        order_by: str = "desc",
    ):
        """Get all"""
        return self.respository.read(
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            order_by=order_by,
        )

    def get_one(self, model_id: int):
        """Get one"""
        response = self.respository.read_one(model_id=model_id)

        if not response:
            raise TaskNotFoundException(model_id=model_id)

        return response

    def update(self, model_id: int, data: dict):
        """Update"""
        response = self.respository.update(data=data, model_id=model_id)

        if not response:
            raise TaskNotFoundException(model_id=model_id)

        return response

    def create(self, data: dict):
        """Create"""
        return self.respository.create(data=data)
