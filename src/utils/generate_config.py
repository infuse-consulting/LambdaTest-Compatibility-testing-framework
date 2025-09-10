import pandas as pd
import json
import os

def generate_test_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
    data_dir = os.path.join(base_dir, "data") 
    excel_path = os.path.join(data_dir, "test_data.xlsx")
    json_path = os.path.join(data_dir, "test_data.json")

    df = pd.read_excel(excel_path, sheet_name="Devices")
    df = df.fillna("")
    df = df.astype(str)
    df["isRealMobile"] = df["isRealMobile"].apply(
        lambda x: "True" if str(x).strip().upper() == "TRUE" else "False"
    )
    records = df.to_dict(orient="records")
    final_dict = {"data": records}
    with open(json_path, "w") as json_file:
        json.dump(final_dict, json_file, indent=4)
        
if __name__ == "__main__":
    generate_test_data()
