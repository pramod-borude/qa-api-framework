Got it! Here's a **single-block `README.md` content** you can copy-paste directly:

```markdown
# QA API Framework

This is a **Python-based API testing framework** using Flask, Pydantic, Pytest, Allure, and Faker. It provides a **mock user API** and a **full test suite** covering CRUD operations, validation, pagination, and keyword search.

---

## 🏗 Project Structure

```

qa-api-framework/
├── api_common/
│   ├── mock/
│       └── app.py 
│       └── models.py
│   └── users_api.py        # API wrapper for test code
├── common/
│   └── helpers.py
│   └── assertions.py       # Assertion helpers # Flask mock API
├── config/
│   └── config.py
├── reports/                # Allure reports output
├── testcases/
│   └── test_users.py       # All test cases
├── conftest.py  
├── pytest.ini
├── README.md
└── requirements.txt

````

---

## ⚙ Setup Instructions

1. **Clone repository**  
   ```bash
   git clone <repo-url>
   cd qa-api-framework
````

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠 Run Flask Mock API

```bash
python mock/app.py
```

The API runs at: `http://127.0.0.1:5000/api/v1`

---

## 🧪 Run Tests

```bash
pytest --alluredir=reports/
```

* Tests automatically **reset mock data** before each test.
* Faker is used for auto-generating usernames and emails.
* Users wrapper (`apicommon/users_api.py`) simplifies API calls in tests.

---

## 📊 Generate Allure Report

1. **Install Allure CLI** (if not installed)

   ```bash
   brew install allure        # macOS
   scoop install allure       # Windows (Scoop)
   ```

2. **Generate and open report**

   ```bash
   allure serve reports/
   ```

* Opens a browser with detailed test results.

---

## ✅ Features

* Full **CRUD tests** (Create, Read, Update, Delete)
* **Validation checks** for invalid inputs, duplicates, missing fields
* **Pagination and keyword search** tests
* **Auto-reset** USERS for isolated tests
* **Allure integration** for detailed reports
* **Faker** for generating realistic user data
* **Pydantic** for request validation

---

## 📝 Notes

* The framework is **self-contained**; all users are stored in-memory.
* **Reset endpoint** ensures clean state for each test.
* Designed for **easy extension** with more APIs or validations.
