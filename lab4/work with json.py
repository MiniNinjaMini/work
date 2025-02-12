import json
from pathlib import Path

# Load the JSON file
file_path = Path("sample-data.json")
with file_path.open("r", encoding="utf-8") as file:
    data = json.load(file)

#рисую табличку
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<15} {'Speed':<10} {'MTU':<5} ")
print(f"{'-'*50}{' '}{'-'*15}{' '}{'-'*10}{' '}{'-'*5}")

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "N/A")
    speed = attributes.get("speed", "N/A")
    mtu = attributes.get("mtu", "N/A")
   
    
    print(f"{dn:<50} {descr:<15} {speed:<10} {mtu:<5} ")
