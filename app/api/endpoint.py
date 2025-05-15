from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import localSession
from app.crud import operations
from app.schemas import schema

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/expense", response_model=schema.ExpenseBase)
def create_expense(expense: schema.ExpenseBase, db: Session = Depends(get_db)):
    db_expense = operations.create_expense(db=db, expense=expense)
    return db_expense

@router.get("/expense/monthly/{year}/{month}", response_model=schema.MonthlyExpenseDescription)
def get_monthly_expenses(year: int, month: str, db: Session = Depends(get_db)):
    monthly_expense = operations.get_monthly_expenses(db=db, year=year, month=month)
    if not monthly_expense:
        raise HTTPException(status_code=404, detail="Monthly expenses not found")
    return monthly_expense

@router.get("/expense/yearly/{year}", response_model=schema.YearlyExpenseDescription)
def get_yearly_expenses(year: int, db: Session = Depends(get_db)):
    yearly_expense = operations.get_yearly_expenses(db=db, year=year)
    if not yearly_expense:
        raise HTTPException(status_code=404, detail="Yearly expenses not found")
    return yearly_expense

@router.get("/expense", response_model=schema.DateRangeExpense)
def get_expenses_in_date_range(start_date: str, end_date: str, db: Session = Depends(get_db)):
    expenses = operations.get_expense_by_date_range(db=db, start_date=start_date, end_date=end_date)
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found in the given date range")
    return expenses
