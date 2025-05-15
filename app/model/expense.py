from sqlalchemy import Column, Integer, Date, String, Enum

from app.db.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(Date, index=True)
    amount = Column(Integer, index=True)
    description = Column(String, index=True)
    category = Column(Enum("Food", "Transport", "Housing", "Entertainment", "Health", "Education", "Others", name="expense_category"), index=True)
