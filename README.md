# FastAPI CRUD API

A beginner-friendly CRUD API built using Python, FastAPI, and Pydantic.

## Features

- Create items
- Read all items
- Read a single item
- Update items
- Delete items
- Request validation using Pydantic
- Automatic API documentation with Swagger UI
- Error handling using HTTPException

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
fastapi-crud-api/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Run the API

```bash
python -m uvicorn main:app --reload
```

## API Documentation

Once the server is running, open:

http://127.0.0.1:8000/docs

Alternative documentation:

http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/items` | Get all items |
| GET | `/items/{item_id}` | Get a single item |
| POST | `/items/{item_id}` | Create an item |
| PUT | `/items/{item_id}` | Update an item |
| DELETE | `/items/{item_id}` | Delete an item |

## Example Request

### POST `/items/1`

Request body:

```json
{
  "name": "Laptop",
  "price": 50000,
  "in_stock": true
}
```

Example response:

```json
{
  "message": "Item created successfully",
  "item_id": 1,
  "item": {
    "name": "Laptop",
    "price": 50000,
    "in_stock": true
  }
}
```