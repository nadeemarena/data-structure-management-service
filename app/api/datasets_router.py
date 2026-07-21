from fastapi import APIRouter, Depends

from app.api.dataset_schema import DatasetCreate, DatasetSummaryResponse, DatasetDetailResponse
from app.services.dataset_service import DatasetService
from app.dependencies import get_dataset_service


router = APIRouter(
    prefix="/datasets",
    tags=["Datasets Management"]
)


@router.post(
    "",
    summary="Create a dataset",
    description="Creates a new dataset with metadata.",
    response_model=DatasetSummaryResponse
)
async def create_dataset(
    dataset: DatasetCreate,
    service: DatasetService = Depends(
        get_dataset_service
    )
):

    return service.create_dataset(dataset)


@router.get(
    "",
    summary="List datasets",
    description="Lists all available datasets.",
    response_model=list[DatasetSummaryResponse]
)
async def list_datasets(
    
    service: DatasetService = Depends(
        get_dataset_service
    )
):
    return service.get_all_datasets()
    

@router.get("/{dataset_id}",
            summary="Retrieve a dataset",
            description="Retrieves a dataset  by its ID with all its elements.",
            response_model=DatasetDetailResponse)
async def retrieve_dataset(dataset_id: int,
    service: DatasetService = Depends(
        get_dataset_service
    )
):

    return service.get_dataset(dataset_id)
