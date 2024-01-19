import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm", exclude=["parser", "ner"])

# User Input
user_input = input("Describe the Python task or program you want to generate: ")

# Language Understanding
doc = nlp(user_input)

# Code Generation
python_code = ""

for sentence in doc.sents:
    # For each sentence, generate a simple print statement with the nouns as arguments
    nouns = [token.text for token in sentence if token.pos_ == "NOUN"]
    if nouns:
        python_code += f'print({", ".join(nouns)})\n'

# Output the generated Python code
print("Generated Python Code:")
print(python_code)