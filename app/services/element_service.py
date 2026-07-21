from fastapi import HTTPException

from app.data.models import DataElement
from app.api.dataelement_schema import DataElementCreate

from app.data.element_repository import (
    DataElementRepository
)

from app.data.dataset_repository import (
    DatasetRepository
)


ALLOWED_DATA_TYPES = {
    "STRING",
    "INTEGER",
    "DATE",
    "BOOLEAN"
}



class DataElementService:


    def __init__(
        self,
        element_repository: DataElementRepository,
        dataset_repository: DatasetRepository
    ):

        self.element_repository = element_repository
        self.dataset_repository = dataset_repository



    def create_element(
        self,
        dataset_id: int,
        element_request: DataElementCreate
    ):


        # Business rule:
        # Dataset must exist

        dataset = (
            self.dataset_repository.get_by_id(
                dataset_id
            )
        )


        if not dataset:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )


        # Business rule:
        # Validate datatype

        if element_request.data_type not in ALLOWED_DATA_TYPES:

            raise HTTPException(
                status_code=400,
                detail="Unsupported data type"
            )


        # Business rule:
        # Element name unique inside dataset

        existing_element = (
            self.element_repository
            .get_by_name_and_dataset_id(
                element_request.name,
                dataset_id
            )
        )


        if existing_element:

            raise HTTPException(
                status_code=400,
                detail="Element already exists in dataset"
            )


        element = DataElement(
            name=element_request.name,
            data_type=element_request.data_type,
            dataset_id=dataset_id
        )


        return self.element_repository.save(element)



    def get_elements(
        self,
        dataset_id: int
    ):


        dataset = (
            self.dataset_repository.get_by_id(
                dataset_id
            )
        )


        if not dataset:

            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )


        return (
            self.element_repository
            .get_by_dataset_id(dataset_id)
        )


    def find_elements(
        self,
        dataset_id: int | None = None,
        data_type: str | None = None,
        is_pii: bool | None = None,
        search: str | None = None
    ):

        return self.element_repository.find_elements(
            dataset_id=dataset_id,
            data_type=data_type,
            is_pii=is_pii,
            search=search
        )

    