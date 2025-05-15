# Expense Model (`app/model/expense.py`)

This section documents the `Expense` model used in the application.

## Overview

The `Expense` model represents an individual expense record in the system. It is defined using SQLModel and includes the following fields:

| Field            | Type          | Description                                             |
|------------      |---------------|-------------------------------------------------- ------|
| `id`             | Optional[int] | Unique identifier (primary key, auto-incremented)       |
| `description`    | str           | Title or description of the expense                     |
| `amount`         | float         | Amount spent                                            |
| `category`       | str (enum)    | Category of the expense (e.g., Food, Travel, Utilities) |
| `timestamp`      | datetime      | Date and time of the expense                            |

