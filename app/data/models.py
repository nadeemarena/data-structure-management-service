from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    Enum,
    DateTime,
    ForeignKey,
    func
)

from app.data.enums import *
from sqlalchemy.orm import relationship

from app.infrastructure.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    description = Column(
        String,
        nullable=False
    )

    owner = Column(
        String,
        nullable=False
    )

    domain = Column(
        String,
        nullable=False
    )

    retention_period_days = Column(
        Integer,
        nullable=False,
        default=30
    )
    elements = relationship(
        "DataElement",
        back_populates="dataset",
        cascade="all, delete-orphan"
    )

class DataElement(Base):

    __tablename__ = "data_elements"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    data_type = Column(
        String,
        nullable=False
    )


    dataset_id = Column(
        Integer,
        ForeignKey(
            "datasets.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    is_pii = Column(
        Boolean,
        nullable=False,
        default=False
    )
    dataset = relationship(
        "Dataset",
        back_populates="elements"
    )