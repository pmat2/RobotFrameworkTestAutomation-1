# Robot Framework CRM Test Automation

A comprehensive test automation project built with [Robot Framework](https://robotframework.org/) to test a CRM (Customer Relationship Management) application.

## Overview

This project contains automated test cases for the [Automation Playground CRM](https://automationplayground.com/crm/) application. It focuses on testing critical functionality including home page loading, user authentication, and session management using Robot Framework with SeleniumLibrary.

## Project Structure

```
.
├── tests/
│   ├── CRM.robot              # Main test suite for CRM application
│   └── embedded/
│       ├── alarm_tests.robot  # Robot Framework tests for embedded app
│       └── app_driver.py      # Python driver for embedded application
├── embedded/
│   ├── app.c                  # Embedded application source code
│   └── hal_temperature_mock.c # Mock hardware abstraction layer
├── results/                   # Test execution reports (generated)
├── pyproject.toml            # Project configuration and dependencies
└── README.md                 # This file
```

## Prerequisites

- **Python**: 3.14 or higher
- **Chrome Browser**: Required for test execution
- **Robot Framework**: 7.4.1
- **SeleniumLibrary**: 6.8.0

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Robot_udemy
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -e .
   ```

## Test Cases

The project includes the following test cases:

| Test ID | Name | Category | Description |
|---------|------|----------|-------------|
| 1001 | Home page should load | Smoke | Verifies the CRM home page loads correctly |
| 1002 | Login should succeed with valid credentials | Smoke | Tests successful login with valid email and password |
| 1003 | Login should fail with missing credentials | Functional | Validates login form rejects empty credentials |
| 1004 | "Remember me" checkbox should persist email | Functional | Tests email persistence with "Remember me" option |
| 1005 | Should be able to log out | Functional | Verifies logout functionality works correctly |
| 1006 | Customers page should display multiple customers | Smoke | Confirms customers grid displays multiple records |
| 1007 | Should be able to add new customer | Smoke | Tests adding a new customer with valid data |
| 1008 | Should be able to cancel adding new customer | Functional | Verifies cancel button works on add customer form |

## Running Tests

### CRM Application Tests

#### Run all tests:
```bash
robot -d results tests
```

#### Run specific test by name:
```bash
robot --test "Login should succeed with valid credentials" tests/CRM.robot
```

#### Run tests by tag:
```bash
robot --include Smoke tests/CRM.robot
robot --include Functional tests/CRM.robot
```

#### Run with specific options:
```bash
robot --variable BROWSER:firefox tests/CRM.robot
robot --outputdir results tests/CRM.robot
```

### Embedded Application Tests

#### Build the embedded application:
```bash
gcc app.c hal_temperature_mock.c -o app_test
```

#### Run embedded tests:
```bash
robot -d results tests/embedded
```

The embedded test suite includes alarm functionality tests using a mock hardware abstraction layer for temperature sensing.

## Test Configuration

Key variables defined in `CRM.robot`:

- **BROWSER**: Browser type (default: `chrome`)
- **URL**: CRM application URL (https://automationplayground.com/crm/)
- **LOGIN**: Test account email (`admin@automationdemo.com`)
- **PASSWORD**: Test account password

## Reports

After test execution, Robot Framework generates the following files in the `results/` directory:

- `report.html` - HTML test execution report
- `log.html` - Detailed test execution log
- `output.xml` - Machine-readable test results

## Key Libraries Used

- **[SeleniumLibrary](https://robotframework.org/SeleniumLibrary/)**: For browser automation and web element interactions
- **[Robot Framework](https://robotframework.org/)**: Test automation framework with keyword-driven syntax

## CI/CD Integration

This project can be integrated into CI/CD pipelines. Example for GitHub Actions:

```yaml
- name: Run Robot Tests
  run: |
    robot --outputdir results tests/CRM.robot
```

## Troubleshooting

- **WebDriver Issues**: Ensure ChromeDriver is compatible with your Chrome browser version
- **Timeouts**: Adjust the SeleniumLibrary timeout in `CRM.robot` if tests fail intermittently
- **Element Not Found**: Verify the target CRM application is accessible and hasn't changed

## Contact

For questions or issues, please [add contact information]
