import pandas as pd
import json, os

script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, "test_data.xlsx")
df = pd.read_excel(excel_path, sheet_name="Devices")
df = df.fillna("")
df = df.astype(str)
df["isRealMobile"] = df["isRealMobile"].apply(lambda x: "True" if str(x).strip().upper() == "TRUE" else "False")
records = df.to_dict(orient='records')
final_dict = {"data": records}
json_path = os.path.join(script_dir, "test_data.json")
with open(json_path, "w") as json_file:
    json.dump(final_dict, json_file, indent=4)



