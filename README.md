# Android Chrome Mortgage Calculator Automation

This project is a mobile UI automation test framework using **Appium** and **pytest**, targeting Cathay Bank's mortgage calculator mobile web page.

---

## 📁 Project Structure

```
test_mortgage_mobile/
├── pages/                # Page Object layer
├── tests/                # Test cases with pytest + Allure
├── requirements.txt      # Python dependencies
├── pytest.ini            # Pytest configuration
└── README.md             # This file
```

---

## ⚙️ Environment Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure the following are ready:
   - ✅ Android emulator is running
   - ✅ Appium server is started (`http://localhost:4723/wd/hub`)
   - ✅ Chrome browser is installed in the emulator
   - ✅ `JAVA_HOME` is correctly set

---

## 🚀 Run Tests

### Run tests via pytest:
```bash
pytest tests/
```

### Generate & view Allure report:
```bash
pytest tests/ --alluredir allure-results
allure serve allure-results
```

---

## ✅ Covered Test Scenarios

- `test_full_flow`: Normal test flow with all fields filled (city, district, amount, interest rate, term)
- `test_without_amount`: Validation when amount field is empty

Optional additional cases:
- `test_without_interest_rate`
- `test_without_city`
- `test_large_amount_boundary`

---

## 📌 Notes

- To ensure test stability and prevent UI lag issues, `WebDriverWait` is used instead of `sleep()`.
- All assertions are written with `pytest.fail()` to provide better debugging output and control.

---

## 🙋‍♂️ Author

Jamie Peng – QA Engineer  
GitHub: [JamiePeng0324](https://github.com/JamiePeng0324)