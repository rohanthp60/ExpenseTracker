# CRUD Operations (`app/crud/operations.py`)

This section describes the core functions for interacting with the expense database.

---

## 1. Record a New Expense

**Function:** `create_expense()`

- **Inputs:**  
    - Database session  
    - Instance of the `Expense` model

- **Output:**  
    - Status message  
    - ID assigned to the new expense

---

## 2. Get Monthly Report of Expenses

**Function:** `get_monthly_expenses()`

- **Inputs:**  
    - Database session  
    - Year  
    - Month

- **Process:**  
    - Filters expenses by year and month  
    - Groups by category  
    - Sums expenses per category

- **Output:**  
    - `MonthlyExpenseDescription` object  
        - Year  
        - Total expense  
        - Expenses per category

---

## 3. Get Yearly Report of Expenses

**Function:** `get_yearly_expenses()`

- **Inputs:**  
    - Database session  
    - Year

- **Process:**  
    - Filters expenses by year  
    - Groups by category  
    - Sums expenses per category

- **Output:**  
    - `YearlyExpenseDescription` object  
        - Year  
        - Total expense  
        - Expenses per category

---

## 4. Get Expenses Within a Date Range

**Function:** `get_expense_by_date_range()`

- **Inputs:**  
    - Database session  
    - Start date  
    - End date

- **Process:**  
    - Filters expenses within the specified date range

- **Output:**  
    - `DateRangeExpense` object  
        - Date range  
        - Total expense  
        - List of expenses

---

## 5. Get Expense by ID

**Function:** `get_expense_by_id()`

- **Inputs:**  
    - Database session  
    - Expense ID

- **Output:**  
    - The matching expense record

- **Note:**  
    - Primarily used for testing purposes

---
