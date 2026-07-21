from pydantic import BaseModel, Field, field_validator, ConfigDict
from app.data.enums import  DataType
from app.api.dataelement_schema import DataElementResponse

class DatasetCreate(BaseModel):

    name: str = Field(
        examples=["customer"]
    )
    description: str = Field(
        examples=[
            "Customer master dataset"
        ]
    )
    owner: str = Field(
        examples=["data-platform-team"]
    )
    domain: str = Field(
        examples=["customer-domain"]
    )
    retention_period_days: int = Field(
        default=30,
        examples=[30]
    )

    @field_validator(
        "name",
        "description",
        "owner",
        "domain"
    )
    @classmethod
    def validate_non_empty_string(
        cls,
        value: str,
        info
    ):

        value = value.strip()

        if not value:
            raise ValueError(
                f"{info.field_name} cannot be empty"
            )

        if len(value) > 100:
            raise ValueError(
                f"{info.field_name} is too long"
            )

        return value
    


class DatasetSummaryResponse(BaseModel):

    id: int
    name: str
    description: str
    owner: str
    domain: str
    retention_period_days: int    
    model_config = ConfigDict(
        from_attributes=True
    )

class DatasetDetailResponse(BaseModel):

    id: int
    name: str
    description: str
    owner: str
    domain: str
    retention_period_days: int
    elements: list[DataElementResponse] = Field(default_factory=list)
    model_config = ConfigDict(
        from_attributes=True
    )
