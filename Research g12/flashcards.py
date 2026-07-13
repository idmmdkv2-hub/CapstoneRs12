import os
import json
import google.genai as genai

# Setup connection
client = genai.Client(api_key="AQ.Ab8RN6J7CZxd3T-UCaKQzoFF_1rsD4yZbP8kuE-08WaF2KuDvQ")
DECK_FILE = "deck.json"

def fetch_cards_from_ai():
    """Calls the AI once to build a robust collection of cards."""
    print("\n🤖 [AI Builder] Generating fresh flashcards from the cloud...")
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=(
                "Create a study deck of exactly 3 different flashcards for Calculus (Chain Rule). "
                "Format the response strictly as a valid JSON array of objects, like this:\n"
                '[\n  {"q": "Question 1", "a": "Answer 1"},\n  {"q": "Question 2", "a": "Answer 2"}\n]'
            )
        )
        # Clean up code blocks if the AI wraps JSON in ```json
        clean_text = response.text.strip().removeprefix("```json").removesuffix("```").strip()
        return json.loads(clean_text)
    except Exception as e:
        print(f"\n⚠️ API limit hit ({e}). Falling back to built-in emergency starter deck!")
        return [
            {"q": "Find the derivative of f(x) = sin(x^2)", "a": "f'(x) = cos(x^2) * 2x = 2x*cos(x^2)"},
            {"q": "Find the derivative of g(x) = (3x^2 + 1)^5", "a": "g'(x) = 5(3x^2 + 1)^4 * (6x) = 30x*(3x^2 + 1)^4"},
            {"q": "What is the core formula of the Chain Rule?", "a": "If h(x) = f(g(x)), then h'(x) = f'(g(x)) * g'(x)"}
        ]

# --- LOAD OR CREATE DECK ---
if not os.path.exists(DECK_FILE):
    cards = fetch_cards_from_ai()
    with open(DECK_FILE, "w") as f:
        json.dump(cards, f, indent=4)
else:
    print("\n📂 [Local Storage] Loading your saved deck instantly from disk...")
    with open(DECK_FILE, "r") as f:
        cards = json.load(f)

# --- RUN INTERACTIVE CORE ---
print("\n==========================================")
print("       📚 LOCAL SMART DECK SYSTEM         ")
print("==========================================")
print(f" Total active cards in folder: {len(cards)}")
print("==========================================")

for idx, card in enumerate(cards, 1):
    print(f"\n [CARD {idx} of {len(cards)}]")
    print(f" 📝 QUESTION:\n {card['q']}")
    print("-" * 42)
    
    # Wait for student input
    input(" 👉 Press [ENTER] to flip card...")
    
    print(f"\n 💡 SOLUTION STEPS:\n {card['a']}")
    print("=" * 42)
    
    action = input(" Next card? (Type 'q' to quit, or press Enter): ").strip().lower()
    if action == 'q':
        break

print("\n🎉 Study session complete! Your deck is safely saved for next time.\n")
