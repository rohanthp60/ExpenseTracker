# Expense Tracker API

This is a FastAPI-based backend for a simple expense tracking application.

## Features
- RESTful API with FastAPI
- PostgreSQL database with SQLModel
- Dockerized deployment
- Environment-based configuration

## Functionalities
- Record the expense with category information
- Fetches monthly or yearly reports, informing the about the expenditure in each category

## Limitations
- Limited number of api-endpoints
- Deletion of expenses is not allowed
- Lack of concurrency (with small set of functionalities, deemed unnecessary)

## Project Structure

The project is organized as follows:

```text
app/
├── api/         # API route definitions
├── core/        # Application settings and configuration
├── crud/        # Database CRUD operations
├── db/          # Database connection and session management
├── model/       # SQLModel ORM models
├── schemas/     # Pydantic data validation schemas
└── main.py      # Application entry point
```


