import requests
ENDPOINT = 'http://127.0.0.1:8000/'


def test_get_home():
    assert requests.get(ENDPOINT).status_code == 200

def test_create_expense():
    data = {
        "date": "2025/05/14",
        "amount": 55,
        "category": "Food",
        "description": "Bought 0.5 litre ,milk"
    }
    response = requests.post(ENDPOINT + 'expense', json=data)
    assert response.status_code == 200

def test_created_task_exists():
    data = {
        "date": "2025/05/14",
        "amount": 55,
        "category": "Food",
        "description": "Bought 0.5 litre ,milk"
    }
    response = requests.post(ENDPOINT + 'expense', json=data)
    assert response.status_code == 200
    recieved_id = response.json().get('expense_id')
    response = requests.get(ENDPOINT + f'expense/{recieved_id}')
    assert response.status_code == 200
    data['id'] = recieved_id
    for key, value in response.json().items():
        assert data[key] == value

def test_get_monthly_report():
    expenses = [
        {
            "date": "2001/01/15",
            "amount": 20,
            "category": "Transport",
            "description": "Bus fare"
        },
        {
            "date": "2001/03/22",
            "amount": 100,
            "category": "Food",
            "description": "Weekly shopping"
        },
        {
            "date": "2001/12/05",
            "amount": 45,
            "category": "Entertainment",
            "description": "Movie tickets"
        }
    ]
    total_price = 0
    for each in expenses:
        resonse = requests.post(ENDPOINT + 'expense', json=each)
        total_price += each['amount']
        assert resonse.status_code == 200

    response = requests.get(ENDPOINT + 'expense/yearly/2001')
    assert response.status_code == 200
    report = response.json()
    expected_report = {
        "food": 100,
        "transport": 20,
        "housing": 0,
        "entertainment": 45,
        "health": 0,
        "education": 0,
        "others": 0,
        "total": total_price,
        "year": 2001
    }
    assert report == expected_report
    
def test_get_monthly_report_december_2003():
    expenses = [
        {
            "date": "2003/12/01",
            "amount": 75,
            "category": "Food",
            "description": "Groceries"
        },
        {
            "date": "2003/12/15",
            "amount": 40,
            "category": "Transport",
            "description": "Taxi fare"
        },
        {
            "date": "2003/12/20",
            "amount": 60,
            "category": "Entertainment",
            "description": "Concert tickets"
        }
    ]
    total_price = 0
    for each in expenses:
        response = requests.post(ENDPOINT + 'expense', json=each)
        total_price += each['amount']
        assert response.status_code == 200
    response = requests.get(ENDPOINT + 'expense/monthly/2003/12')
    assert response.status_code == 200
    report = response.json()
    expected_report = {
        "food": 75,
        "transport": 40,
        "housing": 0,
        "entertainment": 60,
        "health": 0,
        "education": 0,
        "others": 0,
        "total": total_price,
        "month": 12,
        "year": 2003
    }
    assert report == expected_report


