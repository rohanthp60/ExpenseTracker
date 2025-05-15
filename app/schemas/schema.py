from pydantic import BaseModel, ConfigDict
from sqlalchemy import Column, Integer, String, Date, Enum

'''structure of individual expense record to be inserted in the table Expense'''
class ExpenseBase(BaseModel):
    id: int|None = None
    date: str
    amount: int
    description: str
    category: str = "Others"

    model_config = ConfigDict(from_attributes=True)


'''structure for expense report, to be inherited by monthly and yearly reports'''
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


'''labels off the expense above with the month'''
class MonthlyExpenseDescription(ExpenseDescription):
    year: int
    month: int


'''labels off the expense above with the year'''
class YearlyExpenseDescription(ExpenseDescription):
    year: int

'''not a report, but shows all expenses with in date range, only with total'''
class DateRangeExpense(BaseModel):
    start_date: str
    end_date: str
    total: int = 0
    expenses: list[ExpenseBase] = []
    class Config:
        orm_mode = True
