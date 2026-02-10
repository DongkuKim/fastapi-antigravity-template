# FastAPI Antigravity Template

A production-ready FastAPI (async) template configured with:

- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Web Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **Database**: [SQLAlchemy](https://www.sqlalchemy.org/) (Async) + `asyncpg` (PostgreSQL)
- **Settings**: [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- **Testing**: [pytest](https://docs.pytest.org/) + `pytest-asyncio`
- **Linting/Formatting**: [Ruff](https://docs.astral.sh/ruff/)

## Getting Started

### Prerequisites

- Python 3.13+
- `uv` installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- **PostgreSQL** running locally on port 5432.
  - Quick start with Docker:
    ```bash
    docker run --name postgres-db \
      -e POSTGRES_USER=postgres \
      -e POSTGRES_PASSWORD=postgres \
      -e POSTGRES_DB=app \
      -p 5432:5432 \
      -d postgres:15
    ```

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd fastapi-antigravity-template
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the development server:
   ```bash
   uv run uvicorn app.main:app --reload
   ```

4. Run tests:
   ```bash
   uv run pytest
   ```

## Project Structure

```
app/
├── api/
│   ├── v1/
│   │   ├── endpoints/  # API route handlers
│   │   └── router.py   # API router configuration
│   └── dependencies.py # API dependencies
├── core/               # Core configuration (settings, db, security)
├── models/             # SQLAlchemy models
├── schemas/            # Pydantic models
├── services/           # Business logic
├── repositories/       # Data access layer
└── main.py             # Application entry point
tests/                  # Test suite
```

## Configuration

Environment variables are managed by `.env` file (copied from `.env.example` if available).
See `app/core/config.py` for available settings.
