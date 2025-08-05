""""Database connection and session management module."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry

DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    url=DATABASE_URL,
    connect_args={},
    pool_recycle=300,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

mapper_registry = registry()
Base = mapper_registry.generate_base()


def get_db():
    """independent database session/connectionper request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
