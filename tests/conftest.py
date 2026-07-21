from app.infrastructure.database import SessionLocal

from app.data.dataset_repository import (
    DatasetRepository
)

from app.services.dataset_service import (
    DatasetService
)


import pytest


@pytest.fixture
def dataset_service():

    db = SessionLocal()

    repository = DatasetRepository(
        db
    )

    service = DatasetService(
        repository
    )

    yield service

    db.close()