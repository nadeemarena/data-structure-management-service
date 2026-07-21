from fastapi import HTTPException

from app.data.models import Dataset
from app.api.dataset_schema import DatasetCreate
from app.data.dataset_repository import DatasetRepository


class DatasetService:

    def __init__(
        self,
        repository: DatasetRepository
    ):
        self.repository = repository


    def create_dataset(
        self,
        dataset_request: DatasetCreate
    ):

        # Business rule:
        # Dataset name must be unique

        existing_dataset = (
            self.repository.get_by_name(
                dataset_request.name
            )
        )

        if existing_dataset:
            raise HTTPException(
                status_code=400,
                detail="Dataset already exists"
            )


        dataset = Dataset(
            name=dataset_request.name,
            description=dataset_request.description,                
            owner=dataset_request.owner,            
            domain=dataset_request.domain
        )


        return self.repository.save(dataset)



    def get_dataset(
        self,
        dataset_id: int
    ):

        dataset = (
            self.repository.get_by_id(
                dataset_id
            )
        )


        if not dataset:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )


        return dataset



    def get_all_datasets(self):

        return self.repository.get_all_datasets()



    def delete_dataset(
        self,
        dataset_id: int
    ):

        dataset = (
            self.repository.get_by_id(
                dataset_id
            )
        )


        if not dataset:
            raise HTTPException(
                status_code=404,
                detail="Dataset not found"
            )


        self.repository.delete(dataset)


        return {
            "message": "Dataset deleted successfully"
        }