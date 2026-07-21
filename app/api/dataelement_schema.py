from pydantic import BaseModel, Field, field_validator, ConfigDict
from app.data.enums import  DataType

class DataElementCreate(BaseModel):

    name: str
    data_type: DataType
    is_pii: bool = Field(default=False)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        value = value.strip()

        if not value:
            raise ValueError(
                "Element name cannot be empty"
            )

        if len(value) > 100:
            raise ValueError(
                "Element name too long"
            )

        return value

class DataElementResponse(BaseModel):

    id: int
    name: str
    data_type: DataType
    is_pii: bool
    model_config = ConfigDict(
        from_attributes=True
    )