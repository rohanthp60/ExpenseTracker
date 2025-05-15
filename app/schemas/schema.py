from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, Date, Enum


class ExpenseBase(BaseModel):
    id: int|None = None
    date: str
    amount: int
    description: str
    category: str = "Others"

    model_config = ConfigDict(from_attributes=True)



class ExpenseDescription(BaseModel):
    food: int = 0
    transport: int = 0
    housing: int = 0
    entertainment: int = 0
    health: int = 0
    education: int = 0
    others: int = 0
    total: int = 0

    class Config:
        orm_mode = True

class MonthlyExpenseDescription(ExpenseDescription):
    year: int
    month: int



class YearlyExpenseDescription(ExpenseDescription):
    year: int


class DateRangeExpense(BaseModel):
    start_date: str
    end_date: str
    total: int = 0
    expenses: list[ExpenseBase] = []
    class Config:
        orm_mode = True
