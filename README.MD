# LambdaTest Compatibility and Cross-Browser Testing Framework

## Overview
This project is a Selenium Python automation framework designed for cross-browser and cross-device testing using LambdaTest. It allows execution of test scripts across real and virtual devices on LambdaTest platform.

## Main Features
- Reads test configurations from Excel
  - The framework extracts test environment details such as browser, platform, versions and device name from a structured Excel file without modifying code.
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
Run the script below to load the test configurations from the Excel file:
<pre> python generate_config.py </pre>
Make sure your Excel file includes necessary fields like browser, browserVersion, platform, platformVersion, deviceName, etc.

## Running Tests
Run a test using pytest:
<pre> pytest .\tests\test_name.py -v -s </pre>
The framework will execute the test across all the environments defined in the Excel file.

## License and Plan
- **Platform**: LambdaTest
- **Plan Used**: Under Web automation testing: Web & Mobile Browser on Real Device
- **Pricing**: $158/month

