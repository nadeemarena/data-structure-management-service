# How To Run

## Clone the repository:
``` bash
git clone https://github.com/nadeemarena/data-structure-management-service.git
cd data-structure-management-service
```
### Using Docker 

``` bash

docker compose build
docker compose up api 
docker compose run tests
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