from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from datetime import date

from app.model.expense import Expense
from app.schemas import schema


def create_expense(db: Session, expense: schema.ExpenseBase) -> int:
    db_expense = Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense.id

def get_monthly_expenses(db: Session, year: int, month: str) -> schema.MonthlyExpenseDescription:
    total_amount = func.sum(Expense.amount).label("total_amount")
    category_totals = (
        db.query(Expense.category, total_amount)
        .filter(
            extract('year', Expense.date) == year,
            extract('month', Expense.date) == month
        )
        .group_by(Expense.category)
        .order_by(total_amount.desc())
        .all()
    )

    expense_description = schema.MonthlyExpenseDescription(
        year=year,
        month=month,
        food=0,
        transport=0,
        housing=0,
        entertainment=0,
        health=0,
        education=0,
        others=0,
        total=0
    )

    for category, total in category_totals:
        category = category.lower()
        if category == "food":
            expense_description.food = total
        elif category == "transport":
            expense_description.transport = total
        elif category == "housing":
            expense_description.housing = total
        elif category == "entertainment":
            expense_description.entertainment = total
        elif category == "health":
            expense_description.health = total
        elif category == "education":
            expense_description.education = total
        else:
            expense_description.others += total

        expense_description.total += total

    return expense_description

def get_yearly_expenses(db: Session, year: int):
    total_amount = func.sum(Expense.amount).label("total_amount")
    category_totals = (
        db.query(Expense.category, total_amount)
        .filter(
            extract('year', Expense.date) == year
        )
        .group_by(Expense.category)
        .order_by(total_amount.desc())
        .all()
    )

    expense_description = schema.YearlyExpenseDescription(
        year=year,
        food=0,
        transport=0,
        housing=0,
        entertainment=0,
        health=0,
        education=0,
        others=0,
        total=0
    )
    for category, total in category_totals:
        if category == "Food":
            expense_description.food = total
        elif category == "Transport":
            expense_description.transport = total
        elif category == "Housing":
            expense_description.housing = total
        elif category == "Entertainment":
            expense_description.entertainment = total
        elif category == "Health":
            expense_description.health = total
        elif category == "Education":
            expense_description.education = total
        else:
            expense_description.others += total

        expense_description.total += total
    return expense_description

def get_expense_by_date_range(db: Session, start_date: str, end_date: str) -> schema.DateRangeExpense:
    expenses = (
        db.query(Expense)
        .filter(Expense.date.between(start_date, end_date))
        .all()
    )
    
    total_amount = sum(expense.amount for expense in expenses)


    expense_list = [
        schema.ExpenseBase.model_validate({
            "id": expense.id,
            "description": expense.description,
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date.strftime("%Y/%m/%d") if isinstance(expense.date, date) else str(expense.date)
        })
        for expense in expenses
    ]

    return schema.DateRangeExpense(
        start_date=start_date,
        end_date=end_date,
        total=total_amount,
        expenses=expense_list
    )

def get_expense_by_id(db: Session, expense_id: int) -> schema.ExpenseBase | None:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None:
        return None
    return schema.ExpenseBase.model_validate({
        "id": expense.id,
        "description": expense.description,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date.strftime("%Y/%m/%d") if isinstance(expense.date, date) else str(expense.date)
    })
