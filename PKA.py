from wikipedia import summary, set_lang
from colorama import Fore, Style, init

# Initialize colorama for cross-platform compatibility
init(autoreset=True)

set_lang("en")

print(Fore.GREEN + "Welcome to Python Knows Anything. Please ask question (in one word).")

while True:
    question = input("")
    if question.lower() == "exit":
        break
    try:
        print("\n", summary(question))
    except Exception as e:
        print(Fore.RED + "An error occurred: " + str(e))

		
