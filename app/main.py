from fastapi import FastAPI

from app.api import datasets_router, elements_router
from app.data.models import Dataset
from app.infrastructure.database import Base, engine


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Data Management Service",
    description="""
    A service for managing datasets and their associated data elements. 
    Features:
    - Dataset management
    - Data element management
    - Metadata validation
    - PII support""",
    version="1.0.0"
)


app.include_router(
    datasets_router.router
)


app.include_router(
    elements_router.router
)