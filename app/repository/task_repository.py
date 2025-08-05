"""Task Repository"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database.database_repository import DatabaseRepository
from app.core.database.session import get_db


class TaskRepository(DatabaseRepository):

    def __init__(self, database: Session = Depends(get_db)):
        super().__init__(None, database)
