# Automated UI Testing for "Staff Clothes"

This repository contains an automated UI testing framework for the clothing online store [Staff Clothes](https://www.staff-clothes.com/). The project was developed as part of a laboratory assignment to demonstrate skills in building automated test architecture, writing test scenarios, and managing discovered defects.

**[View Detailed HTML Test Report](https://fuw4kr.github.io/AutomatedTestingStaff/)**

---

## Technology Stack

* **Programming Language:** Python 3
* **Automation Tool:** Selenium WebDriver
* **Testing Framework:** Pytest
* **Driver Management:** webdriver-manager
* **Reporting:** pytest-html

## Project Architecture

The framework is built using the **Page Object Model (POM)** pattern, which ensures easy maintenance, avoids code duplication, and clearly separates page logic from the tests themselves.

* `pages/` — contains web application page classes (`HomePage`, `ProductPage`, `CartPage`, `CatalogPage`, etc.). These classes contain locators (XPath, CSS) and methods for interacting with elements (clicks, text input, scrolling). All pages inherit from `BasePage`.
* `tests/` — contains classes with test scenarios. They include direct assertions and test logic. Each test is completely isolated (the browser opens and closes for each test individually via `setup_method` and `teardown_method`).

## Test Scenarios (Coverage)

The following key web application modules were automated:

1. **Cart (`test_cart.py`):**
   * Adding an item to the cart.
   * Clearing the cart.
   * Cart state persistence after a page reload.
   * Validating the maximum quantity limit for a single item.
2. **Catalog (`test_catalog.py`):**
   * Sorting items (from cheap to expensive).
   * Filtering items by size.
3. **Checkout (`test_checkout.py`):**
   * Validating an incorrect phone number in the "Quick Order" form.
4. **Search (`test_search.py`):**
   * Searching with a valid keyword.
   * Searching using special characters.
5. **Form Validation (`test_validation.py`):**
   * Validating the minimum password length during registration.
   * Successful registration with valid data.
   * Verifying the inability to enter letters in the phone number field.
6. **UI and Navigation (`test_scroll.py`, `test_footer.py`):**
   * "Scroll to top" button functionality.
   * Verifying social media links in the footer.
   * Footer accessibility in the presence of infinite scrolling.

## Handling Discovered Bugs (XFAIL)

During the creation of automated tests, real defects were found on the live site. Instead of letting the tests fail (`FAILED`), the professional practice of marking them with `@pytest.mark.xfail(reason="...")` was utilized.

**Examples of discovered defects:**
* **Infinite scroll:** Items in the catalog load infinitely, making it physically impossible for the user to reach the site's footer within a reasonable time limit (`test_footer_accessibility_time_116`).
* **Search validation:** When entering incorrect data (e.g., special characters like `1=1`), the system does not show an "items not found" message but continues to display irrelevant results (`test_search_invalid_item_115`).
* **Cart persistence:** The cart is cleared after a simple page refresh (F5) before the session actually ends (`test_cart_persistence_after_refresh_114`).

## How to Run Tests Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/fuw4kr/AutomatedTestingStaff.git](https://github.com/fuw4kr/AutomatedTestingStaff.git)
