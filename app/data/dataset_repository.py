from app.data.base_repository import BaseRepository
from app.data.models import Dataset


class DatasetRepository(
    BaseRepository[Dataset]
):

    def __init__(self, db):

        super().__init__(
            db,
            Dataset
        )


    def get_by_name(
        self,
        name: str
    ):

        return (
            self.db.query(Dataset)
            .filter(
                Dataset.name == name
            )
            .first()
        )
    
    def get_all_datasets(self):
        return self.db.query(Dataset).all()