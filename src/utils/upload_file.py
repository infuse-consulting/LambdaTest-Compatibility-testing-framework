import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

username=os.getenv("LT_USERNAME")
password=os.getenv("LT_ACCESS_KEY")

def upload_file_to_lambdatest(file_path,username,password):
    print("Uploading file:", file_path)
    url = "https://api.lambdatest.com/automation/api/v1/user-files"
    with open(file_path, 'rb') as f:
        files = {'files': f}
        response = requests.post(url, auth=HTTPBasicAuth(username, password), files=files)
    if response.status_code == 200:
        result = response.json()
        if 'data' in result and len(result['data']) > 0:
            key = result['data'][0]['key']
            return key
        else:
            raise Exception(f"Unexpected response format: {result}")
    else:
        raise Exception(f"File upload failed: {response.status_code} {response.text}")
