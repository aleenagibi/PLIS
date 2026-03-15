import json
import os

DATA_FILE = "data/log_data.json"

def view_concepts():
    if not os.path.exists(DATA_FILE):
        print("No concepts logged yet.")
        return

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    if len(data) == 0:
        print("No concepts logged yet.")
        return

    print("\n--- PLIS: Your Logged Concepts ---\n")
    for i, entry in enumerate(data, start=1):
        print(f"{i}. {entry['concept']} | Confidence: {entry['confidence']}/5 | Date: {entry['date']}")
    
    print(f"\nTotal concepts logged: {len(data)}")

view_concepts()