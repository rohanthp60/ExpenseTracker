# Expense API Test Cases

This document outlines test cases to validate the correctness of the Expense API endpoints.
Prior to the test, the database to be used was truncated.

---

## 1. Home Endpoint

**Test Function:** `test_get_home()`

- **Action:**  
    Send a `GET` request to the root endpoint `/`.
- **Assertions:**  
    - Response status code is **200 OK**.

---

## 2. Create Expense

**Test Function:** `test_create_expense()`

- **Action:**  
    Send a `POST` request to `/expense` with a sample expense JSON payload.
- **Assertions:**  
    - Response status code is **200** (successfully created).

---

## 3. Confirm Existense of Created Expense

**Test Function:** `test_created_task_exists()`

- **Actions:**  
    1. Create an expense via `POST /expense`.
    2. Extract the returned expense ID from the response.
    3. Fetch the expense by sending a `GET` request to `/expense/{id}`.
- **Assertions:**  
    - Response status code is **200**.
    - Fetched expense data matches the data sent during creation (including the ID).

---

## 4. Yearly Report Generation

**Test Function:** `test_get_monthly_report()`

- **Actions:**  
    1. Create multiple expenses for different months in the year **2001** via `POST` requests.
    2. Sum the total amounts during creation.
    3. Fetch the yearly expense report with `GET /expense/yearly/2001`.
- **Assertions:**  
    - Response status code is **200**.
    - Returned JSON report matches expected totals per category and overall total.

---

## 5. Monthly Report Generation

**Test Function:** `test_get_monthly_report_december_2003()`

- **Actions:**  
    1. Create several expenses dated in **December 2003**.
    2. Sum the total amount during creation.
    3. Fetch the monthly expense report with `GET /expense/monthly/2003/12`.
- **Assertions:**  
    - Response status code is **200**.
    - Returned report matches expected category totals, total amount, year, and month.

