# API Endpoints (`app/api/endpoint.py`)

Describes the HTTP endpoints for managing expenses with FastAPI.

1. **Database Dependency: `get_db()`**
    - Manages a database session per request.
    - Opens a session using `localSession()`.
    - Yields the session to endpoint functions.
    - Closes the session automatically after the request.

2. **Create Expense: `POST /expense`**
    - Input: Expense data as per `ExpenseBase` schema.
    - Action: Uses `create_expense` to add a new expense to the database.
    - Output: JSON with success message and new expense ID.

3. **Retrieve Monthly Expenses: `GET /expense/monthly/{year}/{month}`**
    - Input: Path parameters `year` (int), `month` (string).
    - Action: Uses `get_monthly_expenses` to fetch expenses by category for the specified month and year.
    - Output: Data in `MonthlyExpenseDescription` schema.
    - Error: 404 if no data for the given month and year.

4. **Retrieve Yearly Expenses: `GET /expense/yearly/{year}`**
    - Input: Path parameter `year` (int).
    - Action: Uses `get_yearly_expenses` to fetch expenses by category for the specified year.
    - Output: Data in `YearlyExpenseDescription` schema.
    - Error: 404 if no data for the given year.

5. **Retrieve Expenses by Date Range: `GET /expense`**
    - Input: Query parameters `start_date` (string), `end_date` (string).
    - Action: Uses `get_expense_by_date_range` to fetch expenses within the date range.
    - Output: Data in `DateRangeExpense` schema.
    - Error: 404 if no expenses found in the range.

6. **Retrieve Expense by ID: `GET /expense/{id}`**
    - Input: Path parameter `id` (int).
    - Action: Uses `get_expense_by_id` to fetch a specific expense by ID.
    - Output: Data in `ExpenseBase` schema.
    - Error: 404 if no expense with the given ID.
