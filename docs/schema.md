# Data Schemas (`app/schema/schema.py`)

Defines the structure of data used for expenses and reports.

---

## 1. ExpenseBase

**Purpose:** Represents an individual expense record to be inserted into the `Expense` table.

**Fields:**

| Field        | Type    | Description                              | Optional | Default    |
|--------------|---------|------------------------------------------|----------|------------|
| `id`         | int     | Expense ID assigned by the database      | Yes      |            |
| `date`       | string  | Date of the expense                      | No       |            |
| `amount`     | int     | Amount spent                             | No       |            |
| `description`| string  | Description of the expense               | No       |            |
| `category`   | string  | Category of the expense                  | No       | "Others"   |

- Uses Pydantic's `ConfigDict` for model configuration with `from_attributes=True`.

---

## 2. ExpenseDescription

**Purpose:** Base structure for expense reports, used by monthly and yearly reports.

**Fields:**

| Field           | Type   | Description                  | Default |
|-----------------|--------|------------------------------|---------|
| `food`          | int    | Amount spent on food         | 0       |
| `transport`     | int    | Amount spent on transport    | 0       |
| `housing`       | int    | Amount spent on housing      | 0       |
| `entertainment` | int    | Amount spent on entertainment| 0       |
| `health`        | int    | Amount spent on health       | 0       |
| `education`     | int    | Amount spent on education    | 0       |
| `others`        | int    | Amount spent on others       | 0       |
| `total`         | int    | Total amount of expenses     | 0       |

- Configured with `orm_mode=True` for ORM compatibility.

---

## 3. MonthlyExpenseDescription

**Purpose:** Extends `ExpenseDescription` to include reporting period.

**Fields:**

| Field   | Type | Description                |
|---------|------|----------------------------|
| `year`  | int  | Year of the report         |
| `month` | int  | Month of the report        |

---

## 4. YearlyExpenseDescription

**Purpose:** Extends `ExpenseDescription` to include reporting period.

**Fields:**

| Field   | Type | Description                |
|---------|------|----------------------------|
| `year`  | int  | Year of the report         |

---

## 5. DateRangeExpense

**Purpose:** Represents all expenses within a specified date range (detailed list, not a summary report).

**Fields:**

| Field        | Type            | Description                                 | Default |
|--------------|-----------------|---------------------------------------------|---------|
| `start_date` | string          | Start of the date range                     |         |
| `end_date`   | string          | End of the date range                       |         |
| `total`      | int             | Total amount of expenses in the range       | 0       |
| `expenses`   | List[ExpenseBase]| List of individual expenses                |         |

- Configured with `orm_mode=True` for ORM compatibility.

