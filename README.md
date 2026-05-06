# E-Commerce Automation Testing Framework

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.59-green)
![Pytest](https://img.shields.io/badge/Pytest-9.0-orange)
![Tests](https://img.shields.io/badge/Tests-12%20Passing-brightgreen)

An end-to-end automation testing framework for [AutomationExercise.com](https://automationexercise.com), 
built with Python, Playwright, and Pytest following the Page Object Model (POM) design pattern.

---

## Framework Architecture
ecommerce-automation/
│
├── pages/                  # Page Object Model classes
│   ├── home_page.py        # Home page actions and locators
│   ├── login_page.py       # Login/logout actions and locators
│   ├── products_page.py    # Product browsing and cart actions
│   └── cart_page.py        # Cart management actions
│
├── tests/                  # Test suites
│   ├── test_home_page.py   # Home page test cases
│   ├── test_login.py       # Authentication test cases
│   └── test_products_and_cart.py  # Products and cart test cases
│
├── reports/                # Allure test reports
├── conftest.py             # Pytest fixtures and browser setup
├── pytest.ini              # Pytest configuration
└── .env                    # Environment variables (not committed)

---

## Tech Stack

- **Python 3.12** — Core programming language
- **Playwright** — Browser automation library
- **Pytest** — Test framework and runner
- **Allure** — Test reporting
- **python-dotenv** — Environment variable management
- **pytest-rerunfailures** — Automatic retry for flaky tests

---

## Key Features

- **Page Object Model (POM)** — Clean separation of test logic and page interactions
- **Cross-browser ready** — Configured for Chromium, easily extendable to Firefox and WebKit
- **Ad blocking** — Network request interception to block ads and ensure test stability
- **Allure reporting** — Rich visual reports with test timelines and detailed results
- **Flaky test handling** — Automatic retry logic with configurable delay
- **Environment config** — Credentials and URLs managed via .env file

---

## Test Coverage

### Home Page Tests
- Home page loads and logo is visible
- Navigation to login page works

### Authentication Tests
- Valid login with correct credentials
- Invalid login with wrong password
- Invalid login with unregistered email
- Logout functionality

### Products & Cart Tests
- Products page loads successfully
- All products are visible on listing page
- Product search returns relevant results
- Add product to cart
- Remove product from cart
- Cart maintains items for logged-in users

---

## Getting Started

### Prerequisites
- Python 3.8+
- Java JDK (for Allure reports)
- Allure CLI

### Installation

1. Clone the repository
```bash
git clone https://github.com/thekamiyeoladipo/ecommerce-automation.git
cd ecommerce-automation
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

4. Set up environment variables — create a `.env` file in the root:

---

## Running Tests

```bash
# Run all tests
pytest -v

# Run a specific test file
pytest tests/test_login.py -v

# Run a specific test
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

## Generating Reports

```bash
# Run tests and generate Allure results
pytest -v

# Open interactive Allure report
allure serve reports/allure-results
```

---

## Author
**Kamiye Oladipo**  
QA Engineer  
[GitHub](https://github.com/thekamiyeoladipo)
[LinkedIn](www.linkedin.com/in/kamiye-oladipo)

