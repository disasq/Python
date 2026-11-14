import requests
import pandas as pd

url = "https://api.spacexdata.com/v4/launches/past"
launches = requests.get(url, timeout=30).json()

rows = []
for launch in launches:
    if launch.get("success") is None:
        continue
    rows.append({
        "flight_number": launch.get("flight_number"),
        "date_utc": launch.get("date_utc"),
        "name": launch.get("name"),
        "launchpad": launch.get("launchpad"),
        "success": launch.get("success"),
        "payload_ids": launch.get("payloads", []),
        "core_ids": [core.get("core") for core in launch.get("cores", [])],
    })

df = pd.DataFrame(rows)
df.to_csv("falcon9_api_launches.csv", index=False)
print(df.head())
