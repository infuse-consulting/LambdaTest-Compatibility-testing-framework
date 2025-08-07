# LambdaTest Compatibility and Cross-Browser Testing Framework

## Overview
This project is a Selenium-based Python automation framework designed for cross-browser and cross-device testing using the LambdaTest platform. It enables the execution of test scripts across a wide range of real and virtual devices.The framework follows Page Object Model (POM) design pattern, promoting reusability, maintainability.

## Main Features
- Reads test configurations from Excel
  - The framework extracts test environment details such as browser, platform, device name and test URL from a structured Excel file without modifying code.
- Allows Cross-browser and cross-device testing on LambdaTest and Supports both real and virtual devices
- Automatically generates an Excel report with Device/browser/OS info,Test execution status and LambdaTest video session link

## Installation
1. Clone the repository

2. Install dependencies
<pre> pip install -r requirements.txt </pre>

3. Set up LambdaTest credentials
Create a .env file in the root directory:
<pre>LT_USERNAME= your_lambdatest_username
LT_ACCESS_KEY= your_lambdatest_access_key
</pre>

## Configuration
Run the script below to load the test configurations from the **.\data\test_data.xlsx** Excel file:
<pre> python generate_config.py </pre>

- **Devices Sheet**: Reads browser, browserVersion, platform, platformVersion, deviceName, and other test environment parameters.
- **Credentials Sheet**: Reads the test URL for testing.

## Running Tests
Run a test using pytest:
<pre> pytest .\tests\<your_test_file>.py -v -s </pre>

The framework will:
- Execute the test across all environments defined in the Excel file.
- Automatically generate a compatibility test report in Excel format after execution.

## License and Plan
- **Platform**: LambdaTest
- **Plan Used**: Under Web automation testing: Web & Mobile Browser on Real Device
- **Pricing**: $158/month

