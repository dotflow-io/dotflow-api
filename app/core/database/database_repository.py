"""Database Repository for Webservices"""

import logging

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database.session import get_db


class DatabaseRepository:
    """Base View to create helpers common to all Webservices."""

    def __init__(
        self, model_class, database: Session = Depends(get_db)
    ) -> None:
        """Constructor"""
        self.model_class = model_class
        self.database = database

    def read_one(self, model_id: int = None):
        """Read one"""
        return (
            self.database.query(self.model_class)
            .filter(self.model_class.id == model_id)
            .one_or_none()
        )

    def read(
        self,
        offset: int = 0,
        limit: int = 100,
        sort_by: str = "id",
        order_by: str = "desc",
    ):
        """Read"""
        try:
            query = self.database.query(self.model_class)

            if order_by == "desc":
                query = query.order_by(
                    getattr(self.model_class, sort_by).desc()
                )
            else:
                query = query.order_by(
                    getattr(self.model_class, sort_by).asc()
                )

            return query.offset(offset).limit(limit).all()

        except Exception as error:
            logging.error(error)
            raise error

    def create(self, data: dict):
        """Create"""
        try:
            db_data = self.model_class(**data)

            self.database.add(db_data)
            self.database.commit()
            self.database.refresh(db_data)

            return db_data

        except Exception as error:
            logging.error(error)
            raise error

    def update(self, data: dict, model_id: int = None):
        """Update"""
        try:
            query = (
                self.database.query(self.model_class)
                .filter(self.model_class.id == model_id)
                .one_or_none()
            )

            if not query:
                return None

            for item in data:
                if data.get(item) is not None:
                    setattr(query, item, data[item])

            self.database.merge(query)
            self.database.commit()
            self.database.refresh(query)

            return query

        except Exception as error:
            logging.error(error)
            raise error
