from app.data.base_repository import BaseRepository
from app.data.models import DataElement

class DataElementRepository(
    BaseRepository[DataElement]
):

    def __init__(self, db):

        super().__init__(
            db,
            DataElement
        )


    def get_by_dataset_id(
        self,
        dataset_id
    ):

        return (
            self.db.query(DataElement)
            .filter(
                DataElement.dataset_id == dataset_id
            )
            .all()
        )
    
    def get_by_name_and_dataset_id(
        self,
        name: str,
        dataset_id: int
    ):

        return (
            self.db.query(DataElement)
            .filter(
                DataElement.name == name,
                DataElement.dataset_id == dataset_id
            )
            .first()
        )   
    
    def find_elements(
        self,
        dataset_id: int | None = None,
        data_type: str | None = None,
        is_pii: bool | None = None,
        search: str | None = None
    ):

        query = self.db.query(DataElement)

        if dataset_id is not None:
            query = query.filter(
                DataElement.dataset_id == dataset_id
            )

        if data_type is not None:
            query = query.filter(
                DataElement.data_type == data_type
            )

        if is_pii is not None:
            query = query.filter(
                DataElement.is_pii == is_pii
            )

        if search is not None:
            search_pattern = f"%{search}%"
            query = query.filter(
                DataElement.name.ilike(search_pattern)
            )
            print(query)

        return query.all()