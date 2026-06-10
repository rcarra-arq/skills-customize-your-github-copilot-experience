# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by defining endpoints, data models, and request validation.

## 📝 Tasks

### 🛠️ Create the API application

#### Description

Set up a FastAPI application with the required imports, app instance, and a startup route for testing.

#### Requirements
Completed program should:

- Install and import `fastapi` and `uvicorn`.
- Create a `FastAPI()` app instance.
- Add a root endpoint at `/` that returns a welcome JSON message.
- Use `uvicorn` to run the app locally.

### 🛠️ Define data models and validation

#### Description

Create Pydantic models for request payloads and responses so FastAPI can validate incoming data automatically.

#### Requirements
Completed program should:

- Define a Pydantic model for creating a new item with fields such as `name`, `description`, and `price`.
- Define a response model that includes an `id` and the item data.
- Validate request data automatically and return validation errors for invalid input.
- Use example values or default descriptions where appropriate.

### 🛠️ Add CRUD endpoints and error handling

#### Description

Implement create, read, update, and delete endpoints for items, with proper HTTP status codes and error responses.

#### Requirements
Completed program should:

- Add endpoints for `POST /items`, `GET /items/{item_id}`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`.
- Use path parameters for item IDs and return appropriate JSON responses.
- Handle missing items with a `404` response and an error message.
- Return success status codes for create, update, and delete operations.
