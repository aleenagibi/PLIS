import json
import os
from datetime import date

#Path to the data file
DATA_FILE = "data/log_data.json"

def load_existing_data():
    """Load existing data from the JSON file  or return an empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    """Save the updated list of concepts to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def log_concept():
    """Ask the user for input and save a new concept entry."""
    print("\n--- PLIS: Log a Concept ---")
    
    concept = input("What concept did you study? ").strip()
    
    while True:
        try:
            confidence = int(input("Rate your confidence (1 to 5): "))
            if 1 <= confidence <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("That's not a valid number. Try again.")
    
    entry = {
        "concept": concept,
        "confidence": confidence,
        "date": str(date.today())
    }
    
    data = load_existing_data()
    data.append(entry)
    save_data(data)
    
    print(f"\nLogged: '{concept}' with confidence {confidence}/5 on {entry['date']}")

# Run the function
log_concept()