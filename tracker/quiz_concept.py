import json
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

DATA_FILE = "data/log_data.json"

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def load_data():
    if not os.path.exists(DATA_FILE):
        print("No concepts logged yet.")
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def pick_concept(data):
    print("\n--- PLIS: Pick a Concept to Be Quizzed On ---\n")
    for i, entry in enumerate(data, start=1):
        print(f"{i}. {entry['concept']} | Confidence: {entry['confidence']}/5")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the concept: "))
            if 1 <= choice <= len(data):
                return choice - 1
            else:
                print(f"Enter a number between 1 and {len(data)}.")
        except ValueError:
            print("Invalid input. Enter a number.")

def generate_questions(concept):
    print(f"\nGenerating questions for '{concept}'...")
    prompt = f"""
    Generate exactly 3 short-answer quiz questions to test understanding of '{concept}'.
    Format your response exactly like this, with no extra text:
    Q1: <question>
    Q2: <question>
    Q3: <question>
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )
    return response.text.strip()

def parse_questions(raw):
    lines = [line.strip() for line in raw.split("\n") if line.strip().startswith("Q")]
    return lines

def score_answers(questions, concept):
    print("\n--- Answer the Questions ---\n")
    answers = []
    for q in questions:
        print(q)
        answer = input("Your answer: ").strip()
        answers.append(answer)

    scoring_prompt = f"Topic: '{concept}'\nQuestions and answers:\n"
    for i, (q, a) in enumerate(zip(questions, answers), start=1):
        scoring_prompt += f"\n{q}\nAnswer given: {a}\n"

    scoring_prompt += """
    Score each answer as correct or incorrect based on general knowledge.
    Respond in exactly this format with no extra text:
    Q1: correct/incorrect
    Q2: correct/incorrect
    Q3: correct/incorrect
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=scoring_prompt
    )
    results = response.text.strip().split("\n")
    correct = sum(1 for r in results if "correct" in r.lower() and "incorrect" not in r.lower())
    return correct

def update_confidence(data, index, correct):
    score_map = {0: 1, 1: 2, 2: 4, 3: 5}
    new_confidence = score_map[correct]
    old_confidence = data[index]["confidence"]
    data[index]["confidence"] = new_confidence
    print(f"\nResults: {correct}/3 correct")
    print(f"Confidence updated: {old_confidence}/5 → {new_confidence}/5")
    return data

def run_quiz():
    data = load_data()
    if not data:
        return

    index = pick_concept(data)
    concept = data[index]["concept"]

    raw_questions = generate_questions(concept)
    questions = parse_questions(raw_questions)

    if len(questions) < 3:
        print("Gemini didn't return the expected format. Try again.")
        return

    correct = score_answers(questions, concept)
    data = update_confidence(data, index, correct)
    save_data(data)
    print("\nYour progress has been saved.")

run_quiz()