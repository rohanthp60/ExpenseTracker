from fastapi import FastAPI

from app.db.database import engine, Base
from app.api.endpoint import router as api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API!"}