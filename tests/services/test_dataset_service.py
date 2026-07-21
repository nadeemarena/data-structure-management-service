import pytest
import uuid

from fastapi import HTTPException

from app.api.dataset_schema import DatasetCreate


def test_create_dataset_duplicate_name(
    dataset_service
):

    dataset_name = (
        f"pytest_customer_{uuid.uuid4()}"
    )

    dataset = DatasetCreate(
        name=dataset_name,
        description="Customer dataset test",
        owner="test-team",
        domain="testing"
    )


    created_dataset = (
        dataset_service.create_dataset(dataset)
    )

    assert created_dataset.name == dataset_name


    with pytest.raises(
        HTTPException,
        match="Dataset already exists"
    ):

        dataset_service.create_dataset(dataset)