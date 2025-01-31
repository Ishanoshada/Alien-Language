import re

# Define the alien language mapping
alien_language = {
    # Keywords
    "print": "zorp",
    "if": "glorp",
    "elif": "glorpflorp",
    "else": "florp",
    "for": "blorp",
    "while": "slorp",
    "def": "plorp",
    "return": "vorp",
    "import": "zorport",
    "from": "froop",
    "class": "clorp",
    "try": "trorp",
    "except": "exorp",
    "with": "worp",
    "as": "azorp",
    "and": "&zorp",
    "or": "|zorp",
    "not": "!zorp",
    "in": "inzorp",
    "is": "iszorp",
    "None": "Norp",
    "True": "Troorp",
    "False": "Flooorp",

    # Symbols
    "+": "~",
    "-": "~~",
    "*": "~~~",
    "/": "~~~~",
    "=": "==",
    "==": "====",
    "!=": "!!==",
    "<": "<<",
    ">": ">>",
    "<=": "<<==",
    ">=": ">>==",
    "(": "[",  # Translate ( to [
    ")": "]",  # Translate ) to ]
    "{": "<",
    "}": ">",
    "[": "[[",  # Translate [ to [[
    "]": "]]",  # Translate ] to ]]
    ",": "..",
    ":": "::",
    ".": "°",
}



def translate_to_alien(code):
    try:
        lines = code.split('\n')
        alien_code = []
        for line in lines:
            # Handle indentation
            indentation = re.match(r'^\s*', line).group()
            # Translate the rest of the line
            translated_line = line.strip()
            for key, value in alien_language.items():
                translated_line = re.sub(r'\b' + re.escape(key) + r'\b', value, translated_line)
            # Fix parentheses to square brackets
            translated_line = translated_line.replace("(", "[").replace(")", "]")
            alien_code.append(indentation + translated_line)
        return '\n'.join(alien_code)
    except Exception as e:
        return f"Translation error: {e}"
    


def translate_to_python(code):
    try:
        lines = code.split('\n')
        python_code = []
        for line in lines:
            # Handle indentation
            indentation = re.match(r'^\s*', line).group()
            # Translate the rest of the line
            translated_line = line.strip()
            for key, value in alien_language.items():
                translated_line = re.sub(r'\b' + re.escape(value) + r'\b', key, translated_line)
            # Fix brackets
            translated_line = translated_line.replace("[", "(").replace("]", ")")
            python_code.append(indentation + translated_line)
        return '\n'.join(python_code)
    except Exception as e:
        return f"Translation error: {e}"
    

def interactive_mode():
    print("Enter Python code to translate to Alien language. Type 'exit' to quit.")
    while True:
        code = input(">>> ")
        if code.lower() == "exit":
            break
        translated_code = translate_to_alien(code)
        print(translated_code)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Translate Python code to Alien language and vice versa.")
    parser.add_argument("--to-alien", action="store_true", help="Translate Python code to Alien language.")
    parser.add_argument("--to-python", action="store_true", help="Translate Alien language code to Python.")
    parser.add_argument("--input", type=str, help="Input file to translate.")
    parser.add_argument("--output", type=str, help="Output file to save the translation.")
    parser.add_argument("--interactive", action="store_true", help="Start interactive mode.")
    args = parser.parse_args()

    if args.interactive:
        interactive_mode()
        return

    if not args.input:
        print("Error: Input file is required.")
        return

    try:
        with open(args.input, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.")
        return

    if args.to_alien:
        translated_code = translate_to_alien(code)
    elif args.to_python:
        translated_code = translate_to_python(code)
    else:
        print("Error: Specify --to-alien or --to-python.")
        return

    if args.output:
        try:
            with open(args.output, 'w') as file:
                file.write(translated_code)
            print(f"Translation saved to '{args.output}'.")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print(translated_code)

if __name__ == "__main__":
    main()