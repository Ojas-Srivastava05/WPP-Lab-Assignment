import re
from googletrans import Translator

def hindi_tokenizer(text):
    patterns = {
        "url": r"https?://(?:www\.|(?!www))[a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[a-zA-Z0-9()@:%_\+.~#?&//=]*)",
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "date": r"\b(?:\d{1,2}[-/\.]){2}\d{2,4}\b",
        "number": r"\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b|\b\d+/\d+\b",
        "username": r"@[A-Za-z0-9_]+",
        "punctuation": r"[""'“”‘’.,!?;:()\[\]{}<>।॥]",
        "hindi_words": r"[\u0900-\u097F]+",
        "other_words": r"\b[A-Za-z]+\b"
    }
    regex = re.compile("|".join(f"(?P<{key}>{value})" for key, value in patterns.items()))
    tokens = [match.group() for match in regex.finditer(text)]
    return tokens

def main():
    translator = Translator()
    user_input = input("Enter text in English: ")
    translated_text = translator.translate(user_input, src='en', dest='hi').text
    tokens = hindi_tokenizer(translated_text)
    print(tokens)

if __name__ == "__main__":
    main()
