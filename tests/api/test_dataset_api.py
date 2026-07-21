import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_dataset():
    """POST /datasets"""

    # ------------------------
    # Arrange
    # ------------------------
    dataset_name = f"pytest_create_{uuid.uuid4()}"

    # ------------------------
    # Act
    # ------------------------
    response = client.post(
        "/datasets",
        json={
            "name": dataset_name,
            "description": "Dataset created by API test",
            "owner": "pytest",
            "domain": "testing"
        }
    )

    # ------------------------
    # Assert
    # ------------------------
    assert response.status_code == 200

    body = response.json()

    assert body["id"] > 0
    assert body["name"] == dataset_name
    assert body["description"] == "Dataset created by API test"
    assert body["owner"] == "pytest"
    assert body["domain"] == "testing"


def test_list_datasets():
    """GET /datasets"""

    # ------------------------
    # Arrange
    # ------------------------
    dataset_name = f"pytest_list_{uuid.uuid4()}"

    create_response = client.post(
        "/datasets",
        json={
            "name": dataset_name,
            "description": "Dataset used for list API test",
            "owner": "pytest",
            "domain": "testing"
        }
    )

    assert create_response.status_code == 200

    # ------------------------
    # Act
    # ------------------------
    response = client.get("/datasets")

    # ------------------------
    # Assert
    # ------------------------
    assert response.status_code == 200

    datasets = response.json()

    assert isinstance(datasets, list)

    created_dataset = next(
        (
            dataset
            for dataset in datasets
            if dataset["name"] == dataset_name
        ),
        None
    )

    assert created_dataset is not None
    assert created_dataset["description"] == "Dataset used for list API test"
    assert created_dataset["owner"] == "pytest"
    assert created_dataset["domain"] == "testing"


def test_retrieve_dataset():
    """GET /datasets/{dataset_id}"""

    # ------------------------
    # Arrange
    # ------------------------
    dataset_name = f"pytest_retrieve_{uuid.uuid4()}"

    create_response = client.post(
        "/datasets",
        json={
            "name": dataset_name,
            "description": "Dataset used for retrieve API test",
            "owner": "pytest",
            "domain": "testing"
        }
    )

    assert create_response.status_code == 200

    dataset_id = create_response.json()["id"]

    # ------------------------
    # Act
    # ------------------------
    response = client.get(
        f"/datasets/{dataset_id}"
    )

    # ------------------------
    # Assert
    # ------------------------
    assert response.status_code == 200

    body = response.json()

    assert body["id"] == dataset_id
    assert body["name"] == dataset_name
    assert body["description"] == "Dataset used for retrieve API test"
    assert body["owner"] == "pytest"
    assert body["domain"] == "testing"

    # Detail response should always contain the elements collection
    assert "elements" in body
    assert isinstance(body["elements"], list)


    def test_create_dataset_duplicate_name():

      # Arrange
      dataset_name = f"pytest_duplicate_{uuid.uuid4()}"

      payload = {
          "name": dataset_name,
          "description": "Duplicate dataset test",
          "owner": "pytest",
          "domain": "testing"
      }


      # First creation should succeed
      first_response = client.post(
          "/datasets",
          json=payload
      )

      assert first_response.status_code == 200


      # Act - create same dataset again
      second_response = client.post(
          "/datasets",
          json=payload
      )


      # Assert
      assert second_response.status_code == 400

      body = second_response.json()

      assert body["detail"] == "Dataset already exists"