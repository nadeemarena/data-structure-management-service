from fastapi import Depends
from sqlalchemy.orm import Session

from app.infrastructure.database import get_db

from app.data.dataset_repository import DatasetRepository
from app.data.element_repository import DataElementRepository

from app.services.dataset_service import DatasetService
from app.services.element_service import DataElementService


def get_dataset_repository(
    db: Session = Depends(get_db)
):
    return DatasetRepository(db)



def get_element_repository(
    db: Session = Depends(get_db)
):
    return DataElementRepository(db)



def get_dataset_service(
    repository: DatasetRepository = Depends(
        get_dataset_repository
    )
):
    return DatasetService(repository)



def get_element_service(
    element_repository: DataElementRepository = Depends(
        get_element_repository
    ),
    dataset_repository: DatasetRepository = Depends(
        get_dataset_repository
    )
):

    return DataElementService(
        element_repository,
        dataset_repository
    )