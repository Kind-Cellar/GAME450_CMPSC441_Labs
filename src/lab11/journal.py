from transformers import pipeline

# Load the text generation pipeline with a GPT-2 model
generator = pipeline("text-generation", model="gpt2")

def createJournalEntry(rounds, health):
    # Define the prompt for the journal entry
    prompt = f"After winning {rounds} rounds of the life threatening Sword, Arrow, and Fire, I feel victorious. However, as I reflect on the fight, I realize that my victory came at a cost. On a scale of 1 to 100, I would rate my pain level at {100-health}. Here is what happened..."

    # Generate the journal entry
    journal_entry = generator(prompt, max_length=150, truncation=True)[0]["generated_text"]
    print(journal_entry)
    return journal_entry

