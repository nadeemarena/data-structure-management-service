from fastapi import APIRouter, Depends

from app.api.dataelement_schema import DataElementCreate, DataElementResponse
from app.services.element_service import DataElementService
from app.dependencies import get_element_service
from app.data.enums import DataType
from app.api.dataset_schema import DatasetSummaryResponse, DatasetDetailResponse



router = APIRouter(
    prefix="/datasets",
    tags=["Data Elements Management"]
)


@router.post(
    "/{dataset_id}/elements",
    summary="Add a data element to a dataset",
    description="Adds a new data element to the specified dataset.",
    response_model=DataElementResponse
)
def add_element_to_dataset(
    dataset_id: int,
    element: DataElementCreate,
    service: DataElementService = Depends(
        get_element_service
    )
):

    return service.create_element(
        dataset_id,
        element
    )



@router.get(
    "/{dataset_id}/elements",
    summary="List data elements in a dataset",
    description="Lists all data elements associated with the specified dataset.",
    response_model=list[DataElementResponse]
)
def list_elements_in_dataset(
    dataset_id: int,
    service: DataElementService = Depends(
        get_element_service
    )
):

    return service.get_elements(dataset_id)


@router.get("/elements/dataelements", 
            summary="Filtering or Searching",
            description="Filtering or searching data elements based on optional filters.",
            response_model=list[DataElementResponse])
def find_elements(
    dataset_id: int | None = None,
    data_type: DataType | None = None,
    is_pii: bool | None = None,
    search: str | None = None,
    service: DataElementService = Depends(get_element_service),
):
    return service.find_elements(
        dataset_id=dataset_id,
        data_type=data_type,
        is_pii=is_pii,
        search=search,
    )