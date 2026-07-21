from typing import Generic, TypeVar
from sqlalchemy.orm import Session


T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(
        self,
        db: Session,
        model: type[T]
    ):
        self.db = db
        self.model = model


    def save(
        self,
        entity: T
    ):

        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)

        return entity


    def get_by_id(
        self,
        entity_id: int
    ):

        return (
            self.db.query(self.model)
            .filter(
                self.model.id == entity_id
            )
            .first()
        )


    def delete(
        self,
        entity: T
    ):

        self.db.delete(entity)
        self.db.commit()