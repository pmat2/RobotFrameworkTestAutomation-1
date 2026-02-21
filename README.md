# Robot Framework CRM Test Automation

A comprehensive test automation project built with [Robot Framework](https://robotframework.org/) to test a CRM (Customer Relationship Management) application.

## Overview

This project contains automated test cases for the [Automation Playground CRM](https://automationplayground.com/crm/) application. It focuses on testing critical functionality including home page loading, user authentication, and session management using Robot Framework with SeleniumLibrary.

## Project Structure

```
.
├── pyproject.toml
├── README.md
├── embedded/
│   ├── backends/
│   ├── hal/
│   └── interfaces/
├── tests/
│   ├── pytest/
│   │   └── tests/             # pytest tests
│   └── robot/                 # Robot Framework tests
│       ├── interfaces/
│       └── hal/
└── results/                   # Generated test reports
```

## Prerequisites

- **Python**: 3.14 or higher
- **Chrome Browser**: Required for test execution
- **Robot Framework**: 7.4.1
- **SeleniumLibrary**: 6.8.0

## Installation

**Create a virtual environment:**
   ```bash
   # Robot Framework Test Automation

   This repository contains Robot Framework and unit tests used in the Udemy embedded/automation training. It includes web/CRM tests, embedded application tests (HAL + C), hardware backend mocks, and drivers used by Robot test suites.

   ## Prerequisites

   - Python 3.14+
   - Recommended: create and use a virtual environment
   ```

   On CI agents that run on Windows, `spidev` is skipped by default in `pyproject.toml` to avoid Linux-only builds.

   ## Test Cases

   Below are the main Robot tests maintained in this repository. The suite includes web/CRM scenarios, embedded alarm tests, and hardware interface tests that use mock backends by default.

| Test ID | Name | Category | Description                                                                   |
|---------|------|----------|-------------------------------------------------------------------------------|
| 1001 | Home page should load | Smoke | Verifies the CRM home page loads correctly                                    |
| 1002 | Login should succeed with valid credentials | Smoke | Tests successful login with valid email and password                          |
| 1003 | Login should fail with missing credentials | Functional | Validates login form rejects empty credentials                                |
| 1004 | "Remember me" checkbox should persist email | Functional | Tests email persistence with "Remember me" option                             |
| 1005 | Should be able to log out | Functional | Verifies logout functionality works correctly                                 |
| 1006 | Customers page should display multiple customers | Smoke | Confirms customers grid displays multiple records                             |
| 1007 | Should be able to add new customer | Smoke | Tests adding a new customer with valid data                                   |
| 1008 | Should be able to cancel adding new customer | Functional | Verifies cancel button works on add customer form                             |
| 2001 | Alarm triggers when temperature exceeds threshold | Embedded | Verify alarm output becomes active when temperature > threshold (mocked HAL)  |
| 2002 | Alarm releases when temperature returns below threshold | Embedded | Verify alarm output deasserts when temperature falls below threshold          |
| 3001 | UART Boot Test | Embedded | UART Boot Test — sends `BOOT` over UART mock and expects `READY`              |
| 3002 | I2C Register Read Test | Embedded |  I2C Register Read Test — reads register `0` and validates returned value bit |
| 3003 | I2C Write And Read Back | Embedded | I2C Write And Read Back — writes a value to register `16` and reads it back   |
| 3004 | SPI Known Pattern | Embedded | SPI Known Pattern — sends pattern `AA` and expects `55` in response           |
| 3005 | GPIO Toggle Test | Embedded | GPIO Toggle Test — sets GPIO pin high and low and verifies readings           |

   ## Running Tests

   Run all Robot tests and write results to the `results/` directory:

   ```powershell
   robot -d results tests
   ```

   Run just the embedded interface tests:

   ```powershell
   robot -d results tests/robot/interfaces/interfaces_tests.robot
   ```

   Run pytest unit tests:

   ```powershell
   pytest tests/pytest/
   ```

   ## CI Notes

   - The library `pyserial` is required by the real UART backend (`embedded/backends/uart_real.py`). Install `pyserial` on CI agents or keep `use_hw=False` to use mocks.
   - `spidev` is a Linux-only package; `pyproject.toml` already avoids building it on Windows.

   ## Reports

   Robot writes `report.html`, `log.html`, and `output.xml` into the `results/` directory after each run.
