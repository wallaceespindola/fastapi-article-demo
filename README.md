![Python](https://www.python.org/static/community_logos/python-logo-generic.svg)

# FastAPI Article Demo

[![Apache 2.0 License](https://img.shields.io/badge/License-Apache2.0-orange)](LICENSE)
[![Python](https://img.shields.io/badge/Built_with-Python-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688)](https://fastapi.tiangolo.com/)
[![SQLModel](https://img.shields.io/badge/ORM-SQLModel-teal)](https://sqlmodel.tiangolo.com/)
[![Pytest](https://img.shields.io/badge/Testing-Pytest-green)](https://pytest.org/)
[![CI](https://github.com/wallaceespindola/fastapi-article-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/wallaceespindola/fastapi-article-demo/actions/workflows/ci.yml)

This project demonstrates the practical implementation of the concepts covered in the article **"FastAPI in Action: Modern and Asynchronous API Development"**. It showcases best practices for building high-performance, type-safe, and maintainable APIs with FastAPI.

## Features

- **Modern API Design** - RESTful endpoints with automatic data validation
- **Database Integration** - SQLModel ORM with SQLite database
- **Authentication** - JWT-based authentication with OAuth2
- **Background Tasks** - Asynchronous task processing
- **Comprehensive Testing** - Unit tests for all endpoints
- **API Documentation** - Auto-generated Swagger and ReDoc documentation

## Project Structure

```
fastapi-article-demo/
├── app/                      # Application source code
│   ├── __init__.py
│   ├── auth.py               # Authentication logic
│   ├── database.py           # Database connection handling
│   ├── main.py               # FastAPI application instance
│   ├── models.py             # SQLModel data models
│   └── routes/               # API endpoints
│       ├── __init__.py
│       ├── auth.py           # Authentication endpoints
│       ├── background_tasks.py # Background tasks endpoints
│       ├── items.py          # Item management endpoints
│       └── users.py          # User management endpoints
├── tests/                    # Test suite
│   ├── __init__.py
│   └── test_main.py          # Main application tests
├── FastAPI_in_Action.md      # The accompanying article
├── LICENSE                   # Apache 2.0 license
├── Makefile                  # Build and test commands
├── README.md                 # This file
└── pyproject.toml            # Project dependencies and metadata
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wallaceespindola/fastapi-article-demo.git
   cd fastapi-article-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or for development:
   pip install -e .
   ```

4. Install additional required packages:
   ```bash
   pip install python-multipart
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Open your browser and navigate to:
   - API: http://localhost:8000/
   - Interactive Documentation: http://localhost:8000/docs
   - Alternative Documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint            | Description                       |
|--------|---------------------|-----------------------------------|
| GET    | /                   | Root endpoint                     |
| POST   | /token              | Get authentication token          |
| POST   | /users/             | Create a new user                 |
| GET    | /users/{user_id}    | Get user details                  |
| POST   | /items/             | Create a new item                 |
| GET    | /items/{item_id}    | Get item details                  |
| POST   | /tasks/action/      | Execute a background task         |

## Example Requests

### Authentication

```bash
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"
```

### Create a User

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com", "password": "password123"}'
```

### Create an Item

```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"name": "Laptop", "description": "High-performance laptop", "price": 1299.99, "tax": 119.99}'
```

## Testing

Run the test suite:

```bash
pytest
```

## Author

- **Wallace Espindola** - Sr. Software Engineer / Solution Architect / Java & Python Dev
  - [LinkedIn](https://www.linkedin.com/in/wallaceespindola/)
  - [GitHub](https://github.com/wallaceespindola)
  - [Email](mailto:wallace.espindola@gmail.com)
  - [Twitter](https://twitter.com/wsespindola)
  - [Dev Community](https://dev.to/wallaceespindola)
  - [DZone Articles](https://dzone.com/users/1254611/wallacese.html)
  - [LinkedIn Articles](https://www.linkedin.com/in/wallaceespindola/recent-activity/articles/)
  - [Website](https://www.wtechitsolutions.com/)

## License

This project is released under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

Copyright © 2025 [Wallace Espindola](https://github.com/wallaceespindola/).
