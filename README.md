# How To Run

## Clone the repository:
``` bash
git clone https://github.com/nadeemarena/data-structure-management-service.git
cd data-structure-management-service
```
### Using Docker 

``` bash

docker compose build
docker compose run tests
docker compose up api 

```

#### On Local Machine without Docker

##### Prerequisites

-Python 3.11+
-uv package manager
---

##### Installing uv

If `uv` is not installed:

### Linux / macOS

curl -LsSf https://astral.sh/uv/install.sh | sh



---



``` bash
uv sync
source .venv/bin/activate
uv run uvicorn app.main:app --reload
```


```text
http://localhost:8000
```

API documentation:

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# Running Tests
``` bash
uv run pytest -v
```

---






# Architecture

The application follows a layered architecture with clear separation of responsibilities
and also following SOLID design principles whereever i felt it will be good to follow.

```text
                    Client
                       |
                       |
                HTTP REST API
                       |
                       |
        +-----------------------------+
        |          API Layer          |
        |-----------------------------|
                       |
                       |
        +-----------------------------+
        |       Service Layer         |
        |-----------------------------|
                       |
                       |
        +-----------------------------+
        |         Data Layer          |
        |-----------------------------|
                       |
                       |
        +-----------------------------+
        |       Infrastructure        |
        |-----------------------------|
                       |
                       |
                  SQLite DB
```

---

## Request Flow

```text
POST /datasets

Client
  |
  v
datasets_router.py/dataelements_router.py
  |
  v
datasetService.py/element_service.py
  |
  v
dataset_repoistory.py/element_repository.py
  |
  v
database.py
  |
  v
SQLite
```

# Data Model

The service manages datasets and their data elements.

## Dataset

Represents a logical collection of related data.

Attributes:

- id: Primary key
- name: Unique dataset identifier
- description: Dataset purpose
- owner: Responsible team
- domain: Business domain

A dataset can contain multiple data elements.

## DataElement

Represents a column/attribute belonging to a dataset.

Attributes:

- id: Primary key
- name: Element name
- data_type: Data type of the element
- is_pii: Indicates whether the element contains sensitive information
- dataset_id: Foreign key to Dataset

Relationship:

Dataset (1) -------- (*) DataElement

# Design Decisions and Trade-offs

## Repository Pattern

Repositories are used to isolate database access from business logic.

Benefits:
- Easier testing
- Separation of concerns
- Database implementation can be changed later

Trade-off:
- Adds additional abstraction for a small application.

---

## SQLite Database

SQLite was selected for simplicity and local development.

Benefits:
- Zero configuration
- Easy setup
- Suitable for demonstration purposes

Trade-off:
- Not suitable for high concurrency production workloads.

A production deployment could use PostgreSQL.

---

## Synchronous SQLAlchemy

The application uses synchronous SQLAlchemy sessions.

Benefits:
- Simpler implementation
- Easier debugging

Trade-off:
- For very high throughput APIs, async SQLAlchemy could provide better scalability.

---

## Search and Filtering

Data elements support filtering by:

- dataset_id
- data_type
- is_pii

and text search by element name.

Trade-off:
- Current implementation uses database LIKE queries.
- For large-scale metadata catalogs, a search engine such as Elasticsearch/OpenSearch could be considered.