# FastAPI Error Handling Demo

A small production-style FastAPI project demonstrating:

- Clean project structure
- API routes
- Service layer
- Pydantic schemas
- Custom exceptions
- Custom exception handlers
- Validation error handling
- Generic 500 error handling

## Project Structure

```text
fastapi-error-handling/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── users.py
│   ├── services/
│   │   └── user_service.py
│   ├── schemas/
│   │   └── user.py
│   └── exceptions/
│       └── custom_exceptions.py
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

From the project root:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok",
  "message": "API is running"
}
```

### Get User

```http
GET /users/1
```

Response:

```json
{
  "id": 1,
  "name": "Haripriya",
  "email": "haripriya@example.com"
}
```

### User Not Found

Try:

```http
GET /users/100
```

Response:

```json
{
  "error": "USER_NOT_FOUND",
  "message": "User with ID 100 was not found"
}
```

Status code:

```text
404
```

### Validation Error

Try:

```http
GET /users/abc
```

The `user_id` must be an integer.

Response status:

```text
422
```

## Why This Structure?

The application separates responsibilities:

```text
Request
   ↓
Route
   ↓
Service
   ↓
Database
```

### Route Layer

Handles HTTP-related concerns such as:

- URL paths
- Request parameters
- Response models

### Service Layer

Contains business logic.

For example:

```python
user = get_user_by_id(user_id)
```

The route does not need to know how the user is retrieved.

### Schema Layer

Pydantic models define and validate API data.

### Exception Layer

Custom exceptions represent specific application errors.

This makes error responses consistent and easier to maintain.

## Error Handling

This project demonstrates:

| Error | Status | Example |
|---|---:|---|
| User Not Found | 404 | `/users/100` |
| Validation Error | 422 | `/users/abc` |
| Internal Server Error | 500 | Unexpected application error |

## Interview Explanation

If asked why you use a service layer:

> "I separate routing from business logic so that the API layer handles HTTP concerns while the service layer handles business operations. This improves maintainability, testability, and makes it easier to replace the data source later."

If asked why custom exception handlers are useful:

> "They allow the API to return consistent and meaningful error responses instead of exposing internal implementation details."

## Future Improvements

This demo uses in-memory data. In a real application, the service layer could connect to:

- PostgreSQL
- Supabase
- Redis
- External APIs

Additional improvements could include:

- Authentication
- Logging
- Unit tests
- Database integration
- Middleware
- Request IDs
- Structured logging
- Docker
- CI/CD
