import os
import pytest
from dotenv import load_dotenv
load_dotenv()
import json
import subprocess
from selenium import webdriver
from urllib.parse import quote
from src.utils.excel_writer import write_result
from datetime import datetime
import pandas as pd
from src.utils.generate_config import generate_test_data
from src.pages.login_page import LoginPage
from src.core.assertions import Utils

def pytest_sessionstart(session):
    """Generate test_data.json before any tests run"""
    generate_test_data()

def load_test_configs():
    json_file_path = os.path.join(os.path.dirname(__file__), "./src/data/test_data.json")
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"Missing test_data.json at {json_file_path}")
    with open(json_file_path, "r") as f:
        content = f.read().strip()
        if not content:
            raise ValueError(f"test_data.json is empty at {json_file_path}")
        return json.loads(content)["data"]

@pytest.fixture(scope="session",params=load_test_configs())
def device_config(request):
    """Provide device/browser configuration for each test"""
    load_test_configs()
    return request.param

@pytest.fixture()
def dataLoad():
    """Load LambdaTest test URL from environment variables and Excel sheet"""
    username=os.getenv("LT_USERNAME")
    password=os.getenv("LT_ACCESS_KEY")
    df = pd.read_excel("./src/data/test_data.xlsx", sheet_name="Url")
    url = df['url'].iloc[0].strip()
    return [username,password,url]

@pytest.fixture
def setup(driver, dataLoad):
    """Prepare LoginPage, Utils, and URL for tests"""
    _, _, url = dataLoad

    login_page = LoginPage(driver)
    assertion = Utils(driver)
    return login_page, assertion, url

@pytest.fixture(scope="function")
def driver(dataLoad, device_config):
    """Initialize Selenium Remote WebDriver session with LambdaTest capabilities"""
    username = quote(dataLoad[0])
    password = quote(dataLoad[1])
    browser = device_config['browser']
    browserVersion = device_config['browserVersion']
    platformName = device_config['platformName']
    platformVersion = device_config['platformVersion']
    deviceName = device_config['deviceName']
    realDevice = device_config['isRealMobile'].strip().lower() == "true"
    display_device_name = deviceName if deviceName else "Desktop" 

    timestamp = datetime.now().strftime("%d_%H%M%S")
    test_name = f"{display_device_name}_{platformName}_{platformVersion}_{browser}_{browserVersion}_{timestamp}".replace(" ", "_")

    supported_browsers = ['Chrome', 'Edge', 'Safari', 'Firefox']
    if browser not in supported_browsers:
        raise Exception(f"Unsupported browser: {browser}. Supported browsers are: {supported_browsers}")

    capabilities = {
        'LT:Options': {
            "platformName": platformName,
            "deviceName": deviceName,
            "platformVersion": platformVersion,
            "project": "Test Automation",
            "idleTimeout": 180,
            "name": test_name,
            "build": "Compatibility testing",
            "console": True,
            "terminal": True,
            "network": True,
            "visual": True,
            "video": True,
            "isRealMobile":realDevice,
            "upload": True,
            "autoGrantPermissions": True,
            "autoAcceptAlerts": True,
            # "deviceOrientation": "landscape",
            # "uploadMedia":["lt://MEDIA19de236461974158972175f7cbf11020","lt://MEDIA90bf5a6b9323472988082757651b4384"],
        },
        'browserName': browser,
        'browserVersion': browserVersion
    }

    if browser == 'Chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
    elif browser == 'Edge':
        options = webdriver.EdgeOptions()
        options.add_argument("--ignore-certificate-errors")
    elif browser == 'Firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--ignore-certificate-errors")
    elif browser == 'Safari':
        options = webdriver.SafariOptions()
        options.add_argument("--ignore-certificate-errors")

    options.set_capability('LT:Options', capabilities['LT:Options'])
    if realDevice:
        hub_url = f"https://{username}:{password}@mobile-hub.lambdatest.com/wd/hub"
    else:
        hub_url = f"https://{username}:{password}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(
        command_executor=hub_url,
        options=options
    )
    driver.capabilities_dict = capabilities
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """Store test results in report after each test execution"""
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        status = "Passed" if report.passed else "Failed"
        full_test_name = item.name
        test_name = full_test_name.split('[')[0]
        device_config = item.funcargs.get("device_config", {})

        result = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Test Name": test_name,
            "Device Name": "Desktop" if device_config.get("deviceName", "") == "" else device_config.get("deviceName"),
            "Device Type":"Real" if device_config.get("isRealMobile", "").strip().lower() == "true" else "Virtual",
            "Platform Name":device_config.get("platformName",""),           
            "OS Version": device_config.get("platformVersion", ""),
            "Browser Name": device_config.get("browser", ""),
            "Browser Version": device_config.get("browserVersion", ""),
            "Test Status": status,
            "Test Duration" :f"{report.duration:.2f}",
        }
        try:
            driver = item.funcargs.get("driver", None)
            if driver:
                session_id = driver.session_id
                video_url = f"https://automation.lambdatest.com/logs/?sessionID={session_id}"
                result["Video Link"] = video_url

        except Exception as e:
            print(f"Error capturing video or screenshot: {e}")
        write_result(result) 


